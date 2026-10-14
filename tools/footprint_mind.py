"""Footprint of the "mind" sculpture where it meets the grass: the body is sliced at the heights
the blades occupy (ground ~0.4 m + blade height), the slices are merged, and the outside distance
to that shape is stored as a small texture. The grass stops exactly at the outline.

Run with any Python that has numpy (e.g. Blender's):
  /Applications/Blender.app/Contents/MacOS/Blender -b --python tools/footprint_mind.py -- \
      assets/data/figure-mind.json assets/data/figure-footprint-mind.json

Output format matches the prototype's #maskdata: n x n uint8 over world xz in [-ext, ext],
value/255*cap = distance in metres outside the footprint (0 inside).
"""
import sys, json, base64
import numpy as np

src, dst = sys.argv[-2:]
FIG_S, FIG_Y = 15 / 1.8, -0.7 * 15
N, EXT, CAP = 256, 6.5, 2.5
LEVELS = np.arange(0.25, 0.95, 0.05)          # world heights covered by ground + grass near the body

fd = json.load(open(src)); b = base64.b64decode(fd['b64']); v = fd['v']
P = np.frombuffer(b, np.int16, v * 3).reshape(-1, 3) * np.array(fd['ext']) * FIG_S + [0, FIG_Y, 0]
part = np.frombuffer(b, np.uint8, v, v * 9)
I = np.frombuffer(b, np.uint16, fd['i'], v * 10 + fd['pad']).reshape(-1, 3)
T = I[(part[I] == 0).all(1)]                   # body triangles only
A, B, C = P[T[:, 0]], P[T[:, 1]], P[T[:, 2]]

cell = 2 * EXT / N
zc = -EXT + (np.arange(N) + 0.5) * cell        # row centres (z)
xc = -EXT + (np.arange(N) + 0.5) * cell        # column centres (x)
inside = np.zeros((N, N), bool)
for y in LEVELS:
    segs = []
    for p, q, r in ((A, B, C), (B, C, A), (C, A, B)):   # each triangle edge crossing the plane
        s = (p[:, 1] - y) * (q[:, 1] - y) < 0
        t = (y - p[s, 1]) / (q[s, 1] - p[s, 1])
        segs.append((p[s] + (q[s] - p[s]) * t[:, None])[:, [0, 2]])
    # pair the two crossing points of each triangle into a segment
    pts = {}
    for k, (p, q, r) in enumerate(((A, B, C), (B, C, A), (C, A, B))):
        s = np.where((p[:, 1] - y) * (q[:, 1] - y) < 0)[0]
        for i, xz in zip(s, segs[k]):
            pts.setdefault(i, []).append(xz)
    S = np.array([pp[:2] for pp in pts.values() if len(pp) >= 2])   # (m, 2, 2): x,z endpoints
    if not len(S):
        continue
    z0, z1 = S[:, 0, 1], S[:, 1, 1]
    for j, z in enumerate(zc):                 # even-odd scanline fill
        c = (z0 - z) * (z1 - z) < 0
        if not c.any():
            continue
        t = (z - z0[c]) / (z1[c] - z0[c])
        xs = np.sort(S[c, 0, 0] + (S[c, 1, 0] - S[c, 0, 0]) * t)
        for a, bb in zip(xs[0::2], xs[1::2]):
            inside[j, (xc >= a) & (xc <= bb)] = True

# distance (metres) from every cell to the nearest footprint cell
iz, ix = np.nonzero(inside)
pz, px = zc[iz], xc[ix]
gz, gx = np.meshgrid(zc, xc, indexing='ij')
D = np.full(N * N, CAP)
for k in range(0, N * N, 4096):
    d = np.sqrt((gz.ravel()[k:k + 4096, None] - pz[None]) ** 2 + (gx.ravel()[k:k + 4096, None] - px[None]) ** 2)
    D[k:k + 4096] = np.minimum(d.min(1), CAP)
D = D.reshape(N, N); D[inside] = 0
q = np.round(D / CAP * 255).astype(np.uint8)
json.dump({'n': N, 'ext': EXT, 'cap': CAP, 'b64': base64.b64encode(q.tobytes()).decode()}, open(dst, 'w'))
print('wrote', dst, 'footprint %.2f m2, x %.2f..%.2f, z %.2f..%.2f' % (inside.sum() * cell * cell, px.min(), px.max(), pz.min(), pz.max()))
