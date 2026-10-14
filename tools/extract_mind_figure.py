"""Extract the "mind" sculpture (cropped head + two inner heads) from 'portfolio 3d2.blend'
into the compact JSON blob used by the prototypes, and bake the rock terrain into a heightmap.

The new body is the same base mesh as the old figure, so it is aligned onto the old
figure.json (best-fit rotation/scale/offset, ICP). That keeps the grass footprint, hover
shapes, ocean reflection and About framing valid without retuning.

Run with Blender's Python (needs numpy + mathutils):
  /Applications/Blender.app/Contents/MacOS/Blender -b "assets/source/portfolio 3d2.blend" \
      --python tools/extract_mind_figure.py -- assets/data/figure.json assets/data/figure-mind.json assets/data/rocks.json

figure-mind.json: int16 positions, int8 normals, uint8 part id (0 body, 1 outer head, 2 inner head), uint16 indices.
rocks.json: uint8 heightmap of the rock terrain above the water line (metres = value/255*range + lo).
"""
import sys, json, base64
import numpy as np
import bpy
from mathutils.kdtree import KDTree

old_json, dst_fig, dst_rocks = sys.argv[-3:]
FIG_S, FIG_Y = 15 / 1.8, -0.7 * 15           # same as the prototype: 15 m tall, buried to the chest
PARTS = ['Human Base Mesh (Sculpting).001', 'Human Base Mesh (Sculpting).002', 'Human Base Mesh (Sculpting).003']
SUBDIV = [False, True, True]                  # body as modelled (same density as the old figure); heads smoothed once


def to_gl(P):                                 # Blender Z-up -> GL Y-up
    return np.stack([P[:, 0], P[:, 2], -P[:, 1]], 1)


def grab(name, mods):
    o = bpy.data.objects[name]
    saved = [(m, m.show_viewport) for m in o.modifiers]
    for m in o.modifiers:
        if m.type == 'SUBSURF':
            m.show_viewport = mods
    bpy.context.view_layer.update()
    oe = o.evaluated_get(bpy.context.evaluated_depsgraph_get()); me = oe.to_mesh(); me.calc_loop_triangles()
    W = np.array(o.matrix_world)
    P = np.array([v.co for v in me.vertices]) @ W[:3, :3].T + W[:3, 3]
    N = np.array([v.normal for v in me.vertices]) @ np.linalg.inv(W[:3, :3])
    T = np.array([t.vertices for t in me.loop_triangles]); MI = np.array([t.material_index for t in me.loop_triangles])
    oe.to_mesh_clear()
    for m, s in saved:
        m.show_viewport = s
    return to_gl(P), to_gl(N), T, MI


# ---- old figure in prototype world space
fd = json.load(open(old_json)); b = base64.b64decode(fd['b64'])
Wold = np.frombuffer(b, np.int16, fd['v'] * 3).reshape(-1, 3) * np.array(fd['ext']) * FIG_S + [0, FIG_Y, 0]
tree = KDTree(len(Wold))
for i, p in enumerate(Wold):
    tree.insert(p, i)
tree.balance()
nearest = lambda X: (np.array([tree.find(x)[2] for x in X]), np.array([tree.find(x)[1] for x in X]))


def umeyama(A, B):                            # similarity transform A -> B
    ma, mb = A.mean(0), B.mean(0); A0, B0 = A - ma, B - mb
    U, S, Vt = np.linalg.svd(B0.T @ A0 / len(A)); D = np.eye(3)
    if np.linalg.det(U @ Vt) < 0:
        D[2, 2] = -1
    R = U @ D @ Vt; s = np.trace(np.diag(S) @ D) / (A0 ** 2).sum() * len(A)
    return s, R, mb - s * R @ ma


# ---- align the new body onto the old one
body = grab(PARTS[0], False)
Bs = body[0][np.random.default_rng(0).choice(len(body[0]), 3000, replace=False)]
best = None
for yaw in np.linspace(0, 2 * np.pi, 12, endpoint=False):
    c, s_ = np.cos(yaw), np.sin(yaw); R = np.array([[c, 0, s_], [0, 1, 0], [-s_, 0, c]])
    s = np.ptp(Wold[:, 1]) / np.ptp(body[0][:, 1]); t = Wold.mean(0) - s * R @ Bs.mean(0)
    for _ in range(30):
        d, j = nearest(s * Bs @ R.T + t); k = d < np.percentile(d, 90)
        s, R, t = umeyama(Bs[k], Wold[j[k]])
    err = np.median(nearest(s * Bs @ R.T + t)[0])
    if best is None or err < best[0]:
        best = (err, s, R, t)
err, s, R, t = best
print('alignment median error %.3f m, scale %.4f' % (err, s))

# ---- figure blob (prototype-normalised space: world = p*FIG_S + (0,FIG_Y,0))
P_all, N_all, I_all, part = [], [], [], []
for k, name in enumerate(PARTS):
    P, N, T, _ = body if k == 0 else grab(name, SUBDIV[k])
    W = s * P @ R.T + t
    N = N @ R.T; N /= np.linalg.norm(N, axis=1, keepdims=True) + 1e-12
    I_all.append(T + sum(len(p) for p in P_all))
    P_all.append((W - [0, FIG_Y, 0]) / FIG_S); N_all.append(N); part.append(np.full(len(W), k, np.uint8))
    print(name, len(W), 'verts', len(T), 'tris', 'world y %.2f..%.2f' % (W[:, 1].min(), W[:, 1].max()))
P = np.concatenate(P_all); N = np.concatenate(N_all); I = np.concatenate(I_all).ravel(); part = np.concatenate(part)
assert len(P) < 65536
sc = 32767 / np.abs(P).max(0)
blob = np.round(P * sc).astype(np.int16).tobytes() + np.round(N * 127).astype(np.int8).tobytes() + part.tobytes()
pad = len(blob) % 2
blob += b'\0' * pad + I.astype(np.uint16).tobytes()
json.dump({'v': len(P), 'i': len(I), 'ext': (1 / sc).tolist(), 'pad': pad, 'parts': True,
           'b64': base64.b64encode(blob).decode()}, open(dst_fig, 'w'))
print('wrote', dst_fig, len(blob) // 1024, 'KB')

# ---- rocks: the 'Plane' geometry-nodes terrain = rock heightfield (slot 1) + wavy water (slot 2).
# Rock height above the median water line, resampled to a 0.25 m grid in sculpture-aligned space.
P, _, T, MI = grab('Plane', True)
def hmap(m, X0, Z0, CS, n):
    v = np.unique(T[MI == m].ravel()); Q = s * P[v] @ R.T + t
    i = ((Q[:, 0] - X0) / CS).astype(int); j = ((Q[:, 2] - Z0) / CS).astype(int); ok = (i >= 0) & (j >= 0) & (i < n) & (j < n)
    H = np.full((n, n), -99.); np.maximum.at(H, (j[ok], i[ok]), Q[ok, 1]); return H
CS, n = 0.25, 200                              # 50 m square from the middle of the (rotated) 65 m terrain
ctr = (s * P[np.unique(T[MI == 1].ravel())] @ R.T + t).mean(0)
X0, Z0 = ctr[0] - n * CS / 2, ctr[2] - n * CS / 2
rock, water = hmap(1, X0, Z0, CS, n), hmap(2, X0, Z0, CS, n)
assert (rock > -99).all(), 'heightmap has holes'
H = rock - np.median(water)
lo, hi = -1.0, float(H.max())
q = np.round((H.clip(lo, hi) - lo) / (hi - lo) * 255).astype(np.uint8)
json.dump({'n': n, 'cell': CS, 'x0': float(X0), 'z0': float(Z0), 'lo': lo, 'hi': hi, 'b64': base64.b64encode(q.tobytes()).decode()}, open(dst_rocks, 'w'))
print('wrote', dst_rocks, 'rock above water: %.1f%%, peak %.2f m' % ((H > 0).mean() * 100, hi))
