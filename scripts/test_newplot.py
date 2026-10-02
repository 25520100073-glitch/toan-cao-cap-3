# -*- coding: utf-8 -*-
import os, re

filepath = r'C:\Users\khải\.gemini\antigravity\scratch\TCC3\B3_11.html'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# find Plotly.newPlot(
match = re.search(r'Plotly\.newPlot\((.*?)\);', text)
if match:
    args_str = match.group(1)
    print("Found Plotly.newPlot, args length:", len(args_str))
    print(args_str[:200])
else:
    print('Plotly.newPlot not found!')
