# -*- coding: utf-8 -*-
import os, re, glob

BASE_DIR = r"C:\Users\khải\.gemini\antigravity\scratch\TCC3"

def check_all_files():
    files = sorted(glob.glob(os.path.join(BASE_DIR, "B*.html")))
    print(f"Total files found: {len(files)}")
    
    issues = []
    for fpath in files:
        fname = os.path.basename(fpath)
        with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
            text = f.read()
            
        # Separate HTML body content from huge plotly script
        parts = text.split('<div class="plot-container">')
        top_part = parts[0]
        bottom_part = parts[1].split('</script></div></div>')[-1] if len(parts) > 1 and '</script></div></div>' in parts[1] else ""
        
        visible_html = top_part + "\n" + bottom_part
        
        # Check for replacement character or mojibake
        if '' in visible_html:
            issues.append(f"{fname}: Contains replacement char ")
            
        # Check for single $ math
        dollar_matches = re.findall(r'\$[^\$]+\$', visible_html)
        if dollar_matches:
            issues.append(f"{fname}: Uses $...$ inline math ({len(dollar_matches)} instances)")
            
        # Check if MathJax config is present
        if 'inlineMath' not in top_part:
            pass
            
        # Check for solution block
        if 'Lời giải' not in text:
            issues.append(f"{fname}: Missing 'Lời giải'")
            
        # Check for drawing guide
        if 'Hướng dẫn chi tiết cách vẽ hình' not in text:
            issues.append(f"{fname}: Missing drawing guide")
            
        # Check for warning boxes
        if 'Cảnh báo' in visible_html or 'Đang chờ' in visible_html:
            issues.append(f"{fname}: Still contains warning/placeholder")

    for iss in issues:
        print(iss)
    if not issues:
        print("No issues found!")

if __name__ == "__main__":
    check_all_files()
