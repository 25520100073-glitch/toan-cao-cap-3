# -*- coding: utf-8 -*-
import os, re
from update_skipped import replacements, BASE_DIR

def update_file(filename, content_replacement):
    filepath = os.path.join(BASE_DIR, filename + '.html')
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    if filename.startswith('B2'):
        pattern = r'<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">.*?</div>\s*(?=</div>\s*</body>)'
        new_text = re.sub(pattern, lambda m: content_replacement, text, flags=re.DOTALL)
        if new_text == text:
            print(f'Could not replace B2 pattern in {filename}')
        else:
            with open(filepath, 'w', encoding='utf-8') as f: f.write(new_text)
            print(f'Updated {filename}')

    elif filename.startswith('B3'):
        pattern = r'<div class="solution">.*?</div>'
        wrapped = f'<div class="solution">\n{content_replacement}\n</div>'
        new_text = re.sub(pattern, lambda m: wrapped, text, flags=re.DOTALL)
        if new_text == text:
            print(f'Could not replace B3 pattern in {filename}')
        else:
            with open(filepath, 'w', encoding='utf-8') as f: f.write(new_text)
            print(f'Updated {filename}')

for fname, html in replacements.items():
    update_file(fname, html)
