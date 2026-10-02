# -*- coding: utf-8 -*-
import os, json
from inspect_traces_detail import extract_plotly_data, BASE_DIR

for i in range(1, 16):
    fname = f"B3_{i}.html"
    fpath = os.path.join(BASE_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()
    data = extract_plotly_data(text)
    print(f"=== {fname} ===")
    for idx, t in enumerate(data):
        if t.get('type') == 'surface':
            x, y, z = t.get('x'), t.get('y'), t.get('z')
            sx = x.get('shape') if isinstance(x, dict) else f"list({len(x)}x{len(x[0]) if isinstance(x[0], list) else 1})"
            sy = y.get('shape') if isinstance(y, dict) else f"list({len(y)}x{len(y[0]) if isinstance(y[0], list) else 1})"
            sz = z.get('shape') if isinstance(z, dict) else f"list({len(z)}x{len(z[0]) if isinstance(z[0], list) else 1})"
            print(f"  Surface [{idx}] name={t.get('name')} scene={t.get('scene')}: x={sx}, y={sy}, z={sz}")
