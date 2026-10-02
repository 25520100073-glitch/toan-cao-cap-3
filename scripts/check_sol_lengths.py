# -*- coding: utf-8 -*-
import os, re

BASE_DIR = r"C:\Users\khải\.gemini\antigravity\scratch\TCC3"

for prefix, nmax in [("B1", 20), ("B2", 22), ("B3", 15)]:
    for i in range(1, nmax + 1):
        fname = f"{prefix}_{i}.html"
        fpath = os.path.join(BASE_DIR, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            text = f.read()
        if prefix in ["B1", "B2"]:
            m = re.search(r'<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">(.*?)</div>\s*(?=</div>\s*</body>)', text, re.DOTALL)
        else:
            m = re.search(r'<div class="solution">(.*?)</div>', text, re.DOTALL)
        sol = m.group(1).strip() if m else "MISSING"
        print(f"{fname}: len={len(sol)} chars, lines={len(sol.splitlines())}")
