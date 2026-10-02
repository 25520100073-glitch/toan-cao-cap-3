# -*- coding: utf-8 -*-
import os, re
from update_real_problems import BASE_DIR, b2_18, b2_19, b2_22, b3_4

def update_file(filename, solution_html, statement_html):
    filepath = os.path.join(BASE_DIR, filename + '.html')
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    if filename.startswith('B2'):
        text = re.sub(r'<p><strong>Đề bài:</strong>.*?</p>', lambda m: f'<p><strong>Đề bài:</strong> {statement_html}</p>', text)
        pattern = r'<div style="background:#(?:fdedec|eaf4fb); border-left:5px solid #(?:e74c3c|2980b9); padding:20px; margin-top:30px; border-radius:6px;">.*?</div>\s*(?=</div>\s*</body>)'
        text = re.sub(pattern, lambda m: solution_html, text, flags=re.DOTALL)
    else:
        text = re.sub(r'<div class="de-bai"><strong>Đề bài:</strong>.*?</div>', lambda m: f'<div class="de-bai"><strong>Đề bài:</strong> {statement_html}</div>', text)
        pattern = r'<div class="solution">.*?</div>'
        text = re.sub(pattern, lambda m: solution_html, text, flags=re.DOTALL)
        warning_pattern = r'<div style="background:#fdedec; border-left:5px solid #e74c3c; padding:20px; margin-top:30px; border-radius:6px;">.*?</div>\s*(?=<div class="answer-box">)'
        text = re.sub(warning_pattern, lambda m: solution_html, text, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

if __name__ == '__main__':
    st_18 = r"Tính \(\iint_D \sqrt{(4a^2-x^2-y^2)^3} dxdy\) với \(D\) là miền nửa hình tròn tâm \(A(a; 0)\), bán kính \(a > 0\) nằm giữa \(y=x\) và trục \(Oy\) trong góc phần tư thứ nhất."
    update_file("B2_18", b2_18, st_18)
    st_19 = r"Tính \(\iint_D x^2 y dxdy\) với \(D\) là miền phẳng xác định bởi \(2x \le x^2+y^2 \le 4x\) và \(-x \le y \le x\sqrt{3}\)."
    update_file("B2_19", b2_19, st_19)
    st_22 = r"Tính tích phân \(\iint_D xy dxdy\) với \(D\) là hình bình hành với phương trình các cạnh là \(x-y=0, x-y=1, 2x+y=1, 2x+y=3\)."
    update_file("B2_22", b2_22, st_22)
    st_4 = r"Tính tích phân \(\iiint_\Omega \sqrt{x^2+z^2} dxdydz\), trong đó \(\Omega\) là vật thể giới hạn bởi mặt trụ \(x^2+z^2=1\), mặt phẳng \(y+z=2\) và mặt phẳng \(Oxz\)."
    update_file("B3_4", b3_4, st_4)
    print("Files updated with real problem statements and solutions.")
