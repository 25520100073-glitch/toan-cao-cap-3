# -*- coding: utf-8 -*-
import re, json

with open(r'C:\Users\khải\.gemini\antigravity\scratch\TCC3\B3_2.html', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'Plotly\.newPlot\(\s*".*?",\s*(\[.*?\]),\s*(\{.*?\})\s*\)', text, re.DOTALL)
if match:
    layout_str = match.group(2)
    idx = layout_str.find('"scene"')
    print(layout_str[idx:idx+500])
else:
    print("Not found")
