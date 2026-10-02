# -*- coding: utf-8 -*-
import os, json

filepath = r'C:\Users\khải\.gemini\antigravity\scratch\TCC3\B3_11.html'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find("Plotly.newPlot(")
comma_idx = text.find(",", idx)
bracket_idx = text.find("[", comma_idx)

count = 0
end_idx = -1
in_string = False
escape = False
for i in range(bracket_idx, len(text)):
    char = text[i]
    if escape:
        escape = False
        continue
    if char == '\\': escape = True
    elif char == '"': in_string = not in_string
    elif not in_string:
        if char == '[': count += 1
        elif char == ']': count -= 1
        if count == 0:
            end_idx = i
            break

data = json.loads(text[bracket_idx:end_idx+1])
for i, t in enumerate(data):
    if t.get('type') == 'surface':
        z = t.get('z')
        print(f"Surface {i}: z shape = ({len(z)}, {len(z[0])})")
        print(f"  z min = {min(min(row) for row in z)}, z max = {max(max(row) for row in z)}")
        print(f"  name = {t.get('name')}")
        if 'surfacecolor' in t: print("  has surfacecolor")
