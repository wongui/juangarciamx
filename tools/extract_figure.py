"""Extract the sculpture mesh from 'pintura final.glb' into a compact JSON blob
used by the prototypes (int16 positions, int8 normals, uint16 indices, base64).

Usage:  python3 tools/extract_figure.py assets/source/"pintura final.glb" assets/data/figure.json
"""
import sys, json, struct, base64, math
import numpy as np

src, dst = sys.argv[1], sys.argv[2]
f = open(src, 'rb').read()
L = struct.unpack('<I', f[12:16])[0]
j = json.loads(f[20:20 + L])
binoff = 20 + L + 8

def read(ai):
    a = j['accessors'][ai]; bv = j['bufferViews'][a['bufferView']]
    comp = {5126: np.float32, 5123: np.uint16, 5125: np.uint32}[a['componentType']]
    n = {'SCALAR': 1, 'VEC2': 2, 'VEC3': 3}[a['type']]
    off = binoff + bv.get('byteOffset', 0) + a.get('byteOffset', 0)
    arr = np.frombuffer(f, comp, a['count'] * n, off)
    return arr.reshape(-1, n) if n > 1 else arr

# mesh 5 = "FinalBaseMesh" (Human Base Mesh node, rotated 36° around Y in the .blend)
p = j['meshes'][5]['primitives'][0]
P = read(p['attributes']['POSITION']).astype(np.float64)
N = read(p['attributes']['NORMAL']).astype(np.float64)
I = read(p['indices'])
ang = 2 * math.atan2(0.309017, 0.951056)
c, s = math.cos(ang), math.sin(ang)
R = np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])
P = P @ R.T; N = N @ R.T
P[:, 1] -= P[:, 1].min(); P *= 1.8 / P[:, 1].max()          # normalise: feet at 0, 1.8 tall
P[:, 0] -= (P[:, 0].max() + P[:, 0].min()) / 2
P[:, 2] -= (P[:, 2].max() + P[:, 2].min()) / 2
ext = np.abs(P).max(0); sc = 32767 / ext
Pq = np.round(P * sc).astype(np.int16)
Nq = np.round(N / np.linalg.norm(N, axis=1, keepdims=True) * 127).astype(np.int8)
blob = Pq.tobytes() + Nq.tobytes()
pad = len(blob) % 2
blob += b'\0' * pad + I.astype(np.uint16).tobytes()
json.dump({'v': len(P), 'i': len(I), 'ext': (1 / sc).tolist(), 'pad': pad,
           'b64': base64.b64encode(blob).decode()}, open(dst, 'w'))
print('wrote', dst, len(blob) // 1024, 'KB')
