# -*- coding: utf-8 -*-
import os
import re

BASE_DIR = r"C:\Users\khải\.gemini\antigravity\scratch\TCC3"

def fix_html_file(filepath):
    if not os.path.exists(filepath):
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Extract the problem statement for equations
    eq_match = re.search(r'<strong>Đề bài:</strong>\s*(.*?)(?:</p>|</div>)', text, re.DOTALL | re.IGNORECASE)
    equation_text = eq_match.group(1).strip() if eq_match else ""
    # clean up the equation text a bit to make it look like a title
    # if it's very long, maybe just use it directly
    
    # 2. Insert the subtitle before the plot-container HTML div
    # To avoid matching inside plotly.js minified code, we'll only replace the first occurrence
    # or the one that has an explicit HTML structure.
    # Look for `<div class="plot-container">` which is in our template.
    subtitle = f'\n<p style="text-align:center; color:#e67e22; font-weight:bold; margin-bottom:5px;">&#128208; Hình vẽ cho: {equation_text}</p>\n'
    
    # We ensure we only inject it once per file.
    if '&#128208; Hình vẽ cho:' not in text:
        text = text.replace('<div class="plot-container">', subtitle + '<div class="plot-container">', 1)
        
    # 3. Fix Plotly 3D layout to show axes and ticks
    # We only want to modify the layout JSON passed to Plotly.newPlot.
    # Since Plotly.js code is huge, we split by Plotly.newPlot and only replace in the latter part.
    parts = text.split('Plotly.newPlot(')
    if len(parts) > 1:
        prefix = parts[0]
        # the rest contains all the newPlot calls
        suffix = 'Plotly.newPlot(' + parts[1]
        
        # Replace the `false` values for axes in suffix
        suffix = suffix.replace('"showticklabels":false', '"showticklabels":true')
        suffix = suffix.replace('"showgrid":false', '"showgrid":true')
        suffix = suffix.replace('"showbackground":false', '"showbackground":true')
        suffix = suffix.replace('"zeroline":false', '"zeroline":true')
        suffix = suffix.replace('"showline":false', '"showline":true')
        
        text = prefix + suffix

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    
    return True

if __name__ == "__main__":
    count = 0
    for prefix, total in [('B1', 20), ('B2', 22), ('B3', 15)]:
        for i in range(1, total + 1):
            fname = f"{prefix}_{i}.html"
            path = os.path.join(BASE_DIR, fname)
            if fix_html_file(path):
                count += 1
                print(f"Fixed {fname}")
    print(f"Successfully processed {count} files.")
