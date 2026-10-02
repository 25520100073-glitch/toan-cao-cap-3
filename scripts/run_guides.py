# -*- coding: utf-8 -*-
import os, re
from add_drawing_guides import generate_drawing_guide, BASE_DIR

def process_files():
    count = 0
    for prefix, total in [('B1', 20), ('B2', 22), ('B3', 15)]:
        for i in range(1, total + 1):
            fname = f"{prefix}_{i}.html"
            path = os.path.join(BASE_DIR, fname)
            if not os.path.exists(path): continue
            
            print(f"Processing {fname}...", flush=True)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            if '&#127912; Hướng dẫn chi tiết cách vẽ hình' in content:
                print(f"  Already processed {fname}")
                continue
                
            match = re.search(r'&#128208; Hình vẽ cho:\s*(.*?)</p>', content)
            if match:
                eq_text = match.group(1)
                guide = generate_drawing_guide(eq_text)
                
                content = content.replace('<div class="plot-container">', guide + '<div class="plot-container">', 1)
                
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
                print(f"  Updated {fname}")
            else:
                print(f"  No match in {fname}")
    print(f"Added drawing guides to {count} files.")

if __name__ == '__main__':
    process_files()
