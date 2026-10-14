"""Bake ambient occlusion (how hidden each point of the sculpture is) into figure-mind.json, so the
prototype can darken crevices (under the jaw, armpits, around the ears) without dimming the glow.
Each part is occluded only by itself, so the inner heads get no shadow bands when they lift.

Run with Blender's Python (needs numpy + mathutils):
  /Applications/Blender.app/Contents/MacOS/Blender -b --python tools/bake_ao_mind.py -- assets/data/figure-mind.json

Adds 'ao' (base64 uint8 per vertex, 255 = fully open) to the JSON in place.
"""
import sys, json, base64
import numpy as np
from mathutils import Vector
from mathutils.bvhtree import BVHTree

path = sys.argv[-1]
FIG_S, FIG_Y = 15 / 1.8, -0.7 * 15
RAYS, REACH = 48, 1.6                       # rays per vertex, metres a ray travels before counting as open

fd = json.load(open(path)); b = base64.b64decode(fd['b64']); v = fd['v']
P = np.frombuffer(b, np.int16, v * 3).reshape(-1, 3) * np.array(fd['ext']) * FIG_S + [0, FIG_Y, 0]
N = np.frombuffer(b, np.int8, v * 3, v * 6).reshape(-1, 3) / 127.0
N /= np.linalg.norm(N, axis=1, keepdims=True) + 1e-9
part = np.frombuffer(b, np.uint8, v, v * 9)
I = np.frombuffer(b, np.uint16, fd['i'], v * 10 + fd['pad']).reshape(-1, 3)

# cosine-weighted hemisphere directions around +Z (rotated onto each normal below)
rng = np.random.default_rng(1)
u1, u2 = rng.random(RAYS), rng.random(RAYS)
H = np.stack([np.sqrt(u1) * np.cos(2 * np.pi * u2), np.sqrt(u1) * np.sin(2 * np.pi * u2), np.sqrt(1 - u1)], 1)

ao = np.ones(v)
for k in np.unique(part):
    tris = I[(part[I] == k).all(1)]
    bvh = BVHTree.FromPolygons([Vector(p) for p in P], tris.tolist())
    for i in np.where(part == k)[0]:
        n = N[i]; t = np.cross(n, [0, 1, 0] if abs(n[1]) < 0.9 else [1, 0, 0]); t /= np.linalg.norm(t); s = np.cross(n, t)
        o = Vector(P[i] + n * 0.01); hit = 0.0
        for d in H @ np.stack([t, s, n]):
            loc, _, _, dist = bvh.ray_cast(o, Vector(d), REACH)
            if loc is not None:
                hit += 1 - dist / REACH        # near hits darken more than far ones
        ao[i] = 1 - hit / RAYS
    print('part', k, 'mean ao %.3f' % ao[part == k].mean())

fd['ao'] = base64.b64encode(np.round(ao.clip(0, 1) * 255).astype(np.uint8).tobytes()).decode()
json.dump(fd, open(path, 'w'))
print('wrote ao into', path)
