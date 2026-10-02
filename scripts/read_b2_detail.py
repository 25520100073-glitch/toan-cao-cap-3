# -*- coding: utf-8 -*-
import os, re
BASE = r"C:\Users\khải\.gemini\antigravity\scratch\TCC3"
fn = "generate_separated.py"
p = os.path.join(BASE, fn)
with open(p,'r',encoding='utf-8') as f:
    c = f.read()
for search in ['B2_17','B2.17']:
    idx = c.find(search)
    if idx >= 0:
        print(f"Found '{search}' at position {idx}:")
        print(c[idx:idx+800])
        print()
        break
