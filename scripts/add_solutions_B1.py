#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script thêm lời giải vào các file B1_*.html
"""

import os
import re

BASE_DIR = r"C:\Users\khải\.gemini\antigravity\scratch\TCC3"

# Lời giải cho từng bài (HTML với MathJax)
solutions = {

"B1_1": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B1.1</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D (x^2 + xy^3)\\,dxdy\\), với \\(D\\) giới hạn bởi \\(y = x\\) và \\(y = x^2\\).</p>

  <p><strong>Bước 1: Xác định miền D.</strong><br>
  Giao điểm: \\(x = x^2 \\Rightarrow x(x-1)=0 \\Rightarrow x=0,\\; x=1\\).<br>
  Trên \\([0,1]\\): \\(x^2 \\le y \\le x\\).</p>

  <p><strong>Bước 2: Tính tích phân.</strong></p>
  \\[I = \\int_0^1 \\int_{x^2}^{x} (x^2 + xy^3)\\,dy\\,dx\\]

  <p>Tích phân trong theo \\(y\\):</p>
  \\[\\int_{x^2}^{x}(x^2 + xy^3)\\,dy = \\left[x^2 y + x\\frac{y^4}{4}\\right]_{y=x^2}^{y=x}\\]
  \\[= \\left(x^3 + \\frac{x^5}{4}\\right) - \\left(x^4 + \\frac{x^9}{4}\\right) = x^3 - x^4 + \\frac{x^5}{4} - \\frac{x^9}{4}\\]

  <p>Tích phân ngoài theo \\(x\\):</p>
  \\[I = \\int_0^1 \\left(x^3 - x^4 + \\frac{x^5}{4} - \\frac{x^9}{4}\\right)dx\\]
  \\[= \\left[\\frac{x^4}{4} - \\frac{x^5}{5} + \\frac{x^6}{24} - \\frac{x^{10}}{40}\\right]_0^1\\]
  \\[= \\frac{1}{4} - \\frac{1}{5} + \\frac{1}{24} - \\frac{1}{40}\\]

  <p>Quy đồng mẫu số chung là 120:</p>
  \\[= \\frac{30}{120} - \\frac{24}{120} + \\frac{5}{120} - \\frac{3}{120} = \\frac{8}{120} = \\frac{1}{15}\\]

  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = \\dfrac{1}{15}}\\) ✓ Khớp với đáp án.</p>
</div>
""",

"B1_2": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B1.2</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D (x^2 + y)\\,dxdy\\), với \\(D\\) giới hạn bởi \\(y = 4\\) và \\(y = x^2\\).</p>

  <p><strong>Bước 1: Xác định miền D.</strong><br>
  Giao điểm: \\(x^2 = 4 \\Rightarrow x = \\pm 2\\).<br>
  Trên \\([-2,2]\\): \\(x^2 \\le y \\le 4\\).</p>

  <p><strong>Bước 2: Tính tích phân.</strong></p>
  \\[I = \\int_{-2}^{2} \\int_{x^2}^{4} (x^2 + y)\\,dy\\,dx\\]

  <p>Tích phân trong theo \\(y\\):</p>
  \\[\\int_{x^2}^{4}(x^2+y)\\,dy = \\left[x^2 y + \\frac{y^2}{2}\\right]_{x^2}^{4} = \\left(4x^2 + 8\\right) - \\left(x^4 + \\frac{x^4}{2}\\right)\\]
  \\[= 4x^2 + 8 - \\frac{3x^4}{2}\\]

  <p>Tích phân ngoài (hàm chẵn trên \\([-2,2]\\)):</p>
  \\[I = 2\\int_0^2 \\left(4x^2 + 8 - \\frac{3x^4}{2}\\right)dx = 2\\left[\\frac{4x^3}{3} + 8x - \\frac{3x^5}{10}\\right]_0^2\\]
  \\[= 2\\left(\\frac{32}{3} + 16 - \\frac{96}{10}\\right) = 2\\left(\\frac{32}{3} + 16 - \\frac{48}{5}\\right)\\]

  <p>Quy đồng mẫu 15:</p>
  \\[= 2\\cdot\\frac{160 + 240 - 144}{15} = 2\\cdot\\frac{256}{15} = \\frac{512}{15}\\]

  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = \\dfrac{512}{15}}\\) ✓ Khớp với đáp án.</p>
</div>
""",

"B1_3": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B1.3</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\int_0^1 \\int_y^1 e^{x^2}\\,dx\\,dy\\).</p>

  <p><strong>Bước 1: Đổi thứ tự tích phân.</strong><br>
  Miền D: \\(0 \\le y \\le 1\\), \\(y \\le x \\le 1\\) tương đương \\(0 \\le x \\le 1\\), \\(0 \\le y \\le x\\).</p>

  <p><strong>Bước 2: Tính sau khi đổi thứ tự.</strong></p>
  \\[I = \\int_0^1 \\int_0^x e^{x^2}\\,dy\\,dx = \\int_0^1 x\\,e^{x^2}\\,dx\\]

  <p>Đặt \\(u = x^2 \\Rightarrow du = 2x\\,dx\\):</p>
  \\[I = \\frac{1}{2}\\int_0^1 e^u\\,du = \\frac{1}{2}\\left[e^u\\right]_0^1 = \\frac{1}{2}(e - 1)\\]

  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = \\dfrac{e-1}{2}}\\) ✓ Khớp với đáp án \\(\\frac{1}{2}(e-1)\\).</p>
</div>
""",

"B1_4": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B1.4</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D x^3 y\\,dxdy\\), với \\(D\\) là phần tư hình tròn đơn vị \\(x^2+y^2 \\le 1,\\; x\\ge 0,\\; y\\ge 0\\).</p>

  <p><strong>Phương pháp: Tọa độ cực.</strong><br>
  \\(x = r\\cos\\theta,\\; y = r\\sin\\theta,\\; dxdy = r\\,dr\\,d\\theta\\).<br>
  \\(D\\): \\(0 \\le r \\le 1\\), \\(0 \\le \\theta \\le \\pi/2\\).</p>

  \\[I = \\int_0^{\\pi/2}\\int_0^1 (r\\cos\\theta)^3(r\\sin\\theta)\\cdot r\\,dr\\,d\\theta\\]
  \\[= \\int_0^{\\pi/2} \\cos^3\\theta\\sin\\theta\\,d\\theta \\cdot \\int_0^1 r^5\\,dr\\]

  <p>Tích phân theo \\(r\\): \\(\\displaystyle\\int_0^1 r^5\\,dr = \\frac{1}{6}\\).</p>

  <p>Tích phân theo \\(\\theta\\): đặt \\(u=\\cos\\theta\\), \\(du=-\\sin\\theta\\,d\\theta\\):</p>
  \\[\\int_0^{\\pi/2}\\cos^3\\theta\\sin\\theta\\,d\\theta = \\int_1^0 u^3(-du) = \\int_0^1 u^3\\,du = \\frac{1}{4}\\]

  \\[I = \\frac{1}{4}\\cdot\\frac{1}{6} = \\frac{1}{24}\\]

  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = \\dfrac{1}{24}}\\) ✓ Khớp với đáp án.</p>
</div>
""",

"B1_5": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B1.5</h3>
  <p><strong>Đề bài:</strong> Đổi thứ tự tích phân \\(\\displaystyle\\int_0^1 dx\\int_{\\sqrt{x}}^{\\sqrt{2-x^2}} f(x,y)\\,dy\\).</p>

  <p><strong>Bước 1: Xác định miền D.</strong><br>
  Điều kiện: \\(0 \\le x \\le 1\\) và \\(\\sqrt{x} \\le y \\le \\sqrt{2-x^2}\\).<br>
  — Đường dưới: \\(y = \\sqrt{x}\\), tức \\(x = y^2\\) (parabol).<br>
  — Đường trên: \\(y = \\sqrt{2-x^2}\\), tức \\(x^2+y^2 = 2\\) (cung tròn bán kính \\(\\sqrt{2}\\)).</p>

  <p><strong>Giao điểm:</strong> \\(y = \\sqrt{x}\\) và \\(x^2+y^2=2\\):<br>
  \\(x^2 + x = 2 \\Rightarrow (x+2)(x-1)=0 \\Rightarrow x=1, y=1\\).<br>
  Tại \\(x=0\\): \\(y=0\\) (parabol) và \\(y=\\sqrt{2}\\) (cung tròn).<br>
  Miền D nằm giữa parabol \\(y = \\sqrt{x}\\) và cung tròn \\(x^2+y^2=2\\).</p>

  <p><strong>Bước 2: Đổi thứ tự – tích phân theo \\(x\\) trước.</strong><br>
  Với \\(y\\) cố định, \\(y\\) chạy từ \\(0\\) đến \\(\\sqrt{2}\\).<br>
  — Phần 1: \\(0 \\le y \\le 1\\): \\(x\\) từ \\(y^2\\) đến \\(\\sqrt{2-y^2}\\).<br>
  — Phần 2: \\(1 \\le y \\le \\sqrt{2}\\): \\(x\\) từ \\(0\\) đến \\(\\sqrt{2-y^2}\\).</p>

  \\[\\int_0^1 dy\\int_{y^2}^{\\sqrt{2-y^2}} f(x,y)\\,dx + \\int_1^{\\sqrt{2}} dy\\int_0^{\\sqrt{2-y^2}} f(x,y)\\,dx\\]

  <p style="color:#1a5276; font-weight:bold;">Đây là kết quả sau khi đổi thứ tự tích phân.</p>
</div>
""",

"B1_6": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B1.6</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D y\\,dxdy\\), với \\(D\\) giới hạn bởi \\(y = x^2\\) và \\(y = 4 - x^2 + 2x\\).</p>

  <p><strong>Bước 1: Tìm giao điểm.</strong><br>
  \\(x^2 = 4 - x^2 + 2x \\Rightarrow 2x^2 - 2x - 4 = 0 \\Rightarrow x^2 - x - 2 = 0\\)<br>
  \\((x-2)(x+1)=0 \\Rightarrow x = -1,\\; x = 2\\).<br>
  Trên \\([-1,2]\\): \\(x^2 \\le y \\le 4 - x^2 + 2x\\).</p>

  <p><strong>Bước 2: Tính tích phân.</strong></p>
  \\[I = \\int_{-1}^{2} \\int_{x^2}^{4-x^2+2x} y\\,dy\\,dx = \\int_{-1}^{2} \\frac{1}{2}\\left[(4-x^2+2x)^2 - x^4\\right]dx\\]

  <p>Đặt \\(u = 4-x^2+2x\\). Ta có:</p>
  \\[(4-x^2+2x)^2 - x^4 = (4-x^2+2x+x^2)(4-x^2+2x-x^2) = (4+2x)(4-2x^2+2x)\\]
  \\[= 2(2+x)\\cdot2(2-x^2+x) = 4(2+x)(2+x-x^2)\\]

  <p>Khai triển:</p>
  \\[(2+x)(2+x-x^2) = 4+2x-2x^2+2x+x^2-x^3 = 4+4x-x^2-x^3\\]

  \\[I = \\frac{1}{2}\\int_{-1}^{2} 4(4+4x-x^2-x^3)\\,dx = 2\\int_{-1}^{2}(4+4x-x^2-x^3)\\,dx\\]
  \\[= 2\\left[4x + 2x^2 - \\frac{x^3}{3} - \\frac{x^4}{4}\\right]_{-1}^{2}\\]
  \\[= 2\\left[\\left(8+8-\\frac{8}{3}-4\\right) - \\left(-4+2+\\frac{1}{3}-\\frac{1}{4}\\right)\\right]\\]
  \\[= 2\\left[\\left(12-\\frac{8}{3}\\right) - \\left(-2+\\frac{1}{3}-\\frac{1}{4}\\right)\\right]\\]
  \\[= 2\\left[12-\\frac{8}{3}+2-\\frac{1}{3}+\\frac{1}{4}\\right] = 2\\left[14 - 3 + \\frac{1}{4}\\right]\\]

  <p>Quy đồng mẫu 12: \\(14 = \\frac{168}{12}\\), \\(3 = \\frac{36}{12}\\), \\(\\frac{1}{4}=\\frac{3}{12}\\):</p>
  \\[= 2\\cdot\\frac{168-36+3}{12} = 2\\cdot\\frac{135}{12} = \\frac{270}{12} = \\frac{45}{2}\\]

  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = \\dfrac{45}{2}}\\) ✓ Khớp với đáp án.</p>
</div>
""",

"B1_7": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B1.7</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D x^2 y\\,dxdy\\), với \\(D\\) giới hạn bởi parabol \\(y = 3 - x^2\\) và trục \\(Ox\\).</p>

  <p><strong>Bước 1: Xác định miền D.</strong><br>
  Parabol \\(y = 3-x^2\\) cắt trục \\(Ox\\) tại \\(3-x^2=0 \\Rightarrow x = \\pm\\sqrt{3}\\).<br>
  Miền D: \\(-\\sqrt{3} \\le x \\le \\sqrt{3}\\), \\(0 \\le y \\le 3-x^2\\).</p>

  <p><strong>Bước 2: Tính tích phân.</strong></p>
  \\[I = \\int_{-\\sqrt{3}}^{\\sqrt{3}} \\int_0^{3-x^2} x^2 y\\,dy\\,dx\\]

  <p>Tích phân trong theo \\(y\\):</p>
  \\[\\int_0^{3-x^2} x^2 y\\,dy = x^2\\cdot\\frac{(3-x^2)^2}{2}\\]

  <p>Vì \\(x^2(3-x^2)^2\\) là hàm chẵn:</p>
  \\[I = 2\\int_0^{\\sqrt{3}} \\frac{x^2(3-x^2)^2}{2}\\,dx = \\int_0^{\\sqrt{3}} x^2(3-x^2)^2\\,dx\\]

  <p>Khai triển: \\(x^2(3-x^2)^2 = x^2(9-6x^2+x^4) = 9x^2 - 6x^4 + x^6\\)</p>
  \\[I = \\int_0^{\\sqrt{3}} (9x^2 - 6x^4 + x^6)\\,dx = \\left[3x^3 - \\frac{6x^5}{5} + \\frac{x^7}{7}\\right]_0^{\\sqrt{3}}\\]

  <p>Với \\(x = \\sqrt{3}\\): \\(x^3 = 3\\sqrt{3}\\), \\(x^5 = 9\\sqrt{3}\\), \\(x^7 = 27\\sqrt{3}\\):</p>
  \\[I = 3\\cdot3\\sqrt{3} - \\frac{6\\cdot9\\sqrt{3}}{5} + \\frac{27\\sqrt{3}}{7}\\]
  \\[= 9\\sqrt{3} - \\frac{54\\sqrt{3}}{5} + \\frac{27\\sqrt{3}}{7}\\]
  \\[= \\sqrt{3}\\left(9 - \\frac{54}{5} + \\frac{27}{7}\\right)\\]

  <p>Quy đồng mẫu 35: \\(9 = \\frac{315}{35}\\), \\(\\frac{54}{5}=\\frac{378}{35}\\), \\(\\frac{27}{7}=\\frac{135}{35}\\):</p>
  \\[= \\sqrt{3}\\cdot\\frac{315-378+135}{35} = \\sqrt{3}\\cdot\\frac{72}{35} = \\frac{72\\sqrt{3}}{35}\\]

  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = \\dfrac{72\\sqrt{3}}{35}}\\) ✓ Khớp với đáp án.</p>
</div>
""",

"B1_8": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B1.8</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D (x-y)\\,dxdy\\) với \\(D\\) là tam giác \\(A(1,0)\\), \\(B(2,1)\\), \\(C(0,1)\\).</p>

  <p><strong>Bước 1: Tìm phương trình các cạnh.</strong><br>
  — Cạnh AB: qua \\((1,0)\\) và \\((2,1)\\): \\(y = x-1\\), tức \\(x = y+1\\).<br>
  — Cạnh AC: qua \\((1,0)\\) và \\((0,1)\\): \\(y = -x+1\\), tức \\(x = 1-y\\).<br>
  — Cạnh BC: qua \\((2,1)\\) và \\((0,1)\\): \\(y = 1\\).<br>
  Miền D lấy theo \\(y\\) từ \\(0\\) đến \\(1\\), với \\(x\\) từ \\(1-y\\) đến \\(y+1\\).</p>

  <p><strong>Bước 2: Tính tích phân.</strong></p>
  \\[I = \\int_0^1 \\int_{1-y}^{1+y} (x-y)\\,dx\\,dy\\]

  <p>Tích phân trong theo \\(x\\):</p>
  \\[\\int_{1-y}^{1+y}(x-y)\\,dx = \\left[\\frac{x^2}{2}-yx\\right]_{1-y}^{1+y}\\]
  \\[= \\left(\\frac{(1+y)^2}{2} - y(1+y)\\right) - \\left(\\frac{(1-y)^2}{2} - y(1-y)\\right)\\]
  \\[= \\frac{(1+y)^2-(1-y)^2}{2} - y\\left[(1+y)-(1-y)\\right]\\]
  \\[= \\frac{4y}{2} - y\\cdot 2y = 2y - 2y^2\\]

  <p>Tích phân ngoài:</p>
  \\[I = \\int_0^1 (2y-2y^2)\\,dy = \\left[y^2 - \\frac{2y^3}{3}\\right]_0^1 = 1 - \\frac{2}{3} = \\frac{1}{3}\\]

  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = \\dfrac{1}{3}}\\) ✓ Khớp với đáp án.</p>
</div>
""",

"B1_9": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B1.9</h3>
  <p><strong>Đề bài:</strong> Tính diện tích miền D giới hạn bởi \\(y = x^2\\) và \\(y = 2-x^2\\).</p>

  <p><strong>Bước 1: Tìm giao điểm.</strong><br>
  \\(x^2 = 2-x^2 \\Rightarrow 2x^2 = 2 \\Rightarrow x = \\pm 1\\).<br>
  Trên \\([-1,1]\\): \\(x^2 \\le y \\le 2-x^2\\).</p>

  <p><strong>Bước 2: Tính diện tích.</strong></p>
  \\[S = \\iint_D dxdy = \\int_{-1}^{1}\\int_{x^2}^{2-x^2}dy\\,dx = \\int_{-1}^1 (2-x^2-x^2)\\,dx = \\int_{-1}^1(2-2x^2)\\,dx\\]

  <p>Hàm chẵn, nhân đôi:</p>
  \\[S = 2\\int_0^1(2-2x^2)\\,dx = 2\\left[2x - \\frac{2x^3}{3}\\right]_0^1 = 2\\left(2-\\frac{2}{3}\\right) = 2\\cdot\\frac{4}{3} = \\frac{8}{3}\\]

  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{S = \\dfrac{8}{3}}\\) ✓ Khớp với đáp án.</p>
</div>
""",

"B1_10": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B1.10</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D y^2\\,dxdy\\), D giới hạn bởi \\(y=x^2\\), \\(y=2-x\\), trục \\(Ox\\).</p>

  <p><strong>Bước 1: Xác định miền D.</strong><br>
  Giao điểm \\(y=x^2\\) và \\(y=2-x\\): \\(x^2+x-2=0 \\Rightarrow x=1,\\; x=-2\\).<br>
  Giao điểm \\(y=2-x\\) với \\(Ox\\): \\(x=2\\).<br>
  Giao điểm \\(y=x^2\\) với \\(Ox\\): \\(x=0\\).<br>
  Miền D khá phức tạp. Ta chia thành 2 phần theo \\(y\\):<br>
  — Phần 1 (theo x): \\(0 \\le x \\le 1\\), \\(0 \\le y \\le x^2\\): không thuộc D.<br>
  <em>Dùng thứ tự dy dx</em>: Với \\(-2 \\le x \\le 0\\): đường dưới \\(Ox\\) (y=0), đường trên \\(y=x^2\\), nhưng ở đây ta cần kiểm tra lại vị trí tương đối.<br>

  <strong>Phân tích lại:</strong> D là miền nằm giữa ba đường: \\(y=x^2\\) (phía trên), \\(y=2-x\\) và \\(y=0\\) (trục Ox).<br>
  Xét x từ \\(0\\) đến \\(1\\): \\(y\\) từ \\(0\\) đến \\(x^2\\).<br>
  Xét x từ \\(1\\) đến \\(2\\): \\(y\\) từ \\(0\\) đến \\(2-x\\).</p>

  <p><strong>Bước 2: Tính tích phân.</strong></p>
  \\[I = \\int_0^1\\int_0^{x^2} y^2\\,dy\\,dx + \\int_1^2\\int_0^{2-x} y^2\\,dy\\,dx\\]

  <p>Phần 1:</p>
  \\[\\int_0^1 \\frac{x^6}{3}\\,dx = \\frac{1}{3}\\cdot\\frac{1}{7} = \\frac{1}{21}\\]

  <p>Phần 2:</p>
  \\[\\int_1^2 \\frac{(2-x)^3}{3}\\,dx = \\frac{1}{3}\\left[-\\frac{(2-x)^4}{4}\\right]_1^2 = \\frac{1}{3}\\left(0+\\frac{1}{4}\\right) = \\frac{1}{12}\\]

  \\[I = \\frac{1}{21} + \\frac{1}{12} = \\frac{4}{84} + \\frac{7}{84} = \\frac{11}{84}\\]

  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = \\dfrac{11}{84}}\\) ✓ Khớp với đáp án.</p>
</div>
""",

"B1_11": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B1.11</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D xy\\,dxdy\\), D giới hạn bởi \\(y=x^2\\), \\(y=2-x\\), trục \\(Oy\\), \\(x \\ge 0\\).</p>

  <p><strong>Bước 1: Xác định miền D.</strong><br>
  Giao điểm \\(y=x^2\\) và \\(y=2-x\\): \\(x=1\\) (với \\(x\\ge 0\\)).<br>
  Giao điểm \\(y=2-x\\) với \\(Oy\\): \\(x=0,y=2\\).<br>
  Giao điểm \\(y=x^2\\) với \\(Oy\\): \\(x=0,y=0\\).<br>
  Miền D: \\(0\\le x \\le 1\\), \\(x^2 \\le y \\le 2-x\\).</p>

  <p><strong>Bước 2: Tính tích phân.</strong></p>
  \\[I = \\int_0^1\\int_{x^2}^{2-x} xy\\,dy\\,dx = \\int_0^1 x\\cdot\\frac{(2-x)^2-x^4}{2}\\,dx\\]
  \\[= \\frac{1}{2}\\int_0^1 x\\left[(2-x)^2-x^4\\right]dx\\]

  <p>Khai triển:</p>
  \\[x(2-x)^2 = x(4-4x+x^2) = 4x-4x^2+x^3\\]
  \\[I = \\frac{1}{2}\\int_0^1(4x-4x^2+x^3-x^5)\\,dx = \\frac{1}{2}\\left[2x^2-\\frac{4x^3}{3}+\\frac{x^4}{4}-\\frac{x^6}{6}\\right]_0^1\\]
  \\[= \\frac{1}{2}\\left(2-\\frac{4}{3}+\\frac{1}{4}-\\frac{1}{6}\\right)\\]

  <p>Quy đồng mẫu 12: \\(2=\\frac{24}{12}\\), \\(\\frac{4}{3}=\\frac{16}{12}\\), \\(\\frac{1}{4}=\\frac{3}{12}\\), \\(\\frac{1}{6}=\\frac{2}{12}\\):</p>
  \\[= \\frac{1}{2}\\cdot\\frac{24-16+3-2}{12} = \\frac{1}{2}\\cdot\\frac{9}{12} = \\frac{9}{24} = \\frac{3}{8}\\]

  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = \\dfrac{3}{8}}\\) ✓ Khớp với đáp án.</p>
</div>
""",

"B1_12": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B1.12</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D (x+y)\\,dxdy\\), D giới hạn bởi \\(y=x^2\\) và \\(y=2-x\\).</p>

  <p><strong>Bước 1: Giao điểm.</strong><br>
  \\(x^2 = 2-x \\Rightarrow x^2+x-2=0 \\Rightarrow x=-2,\\; x=1\\).<br>
  Trên \\([-2,1]\\): \\(x^2 \\le y \\le 2-x\\).</p>

  <p><strong>Bước 2: Tính tích phân.</strong></p>
  \\[I = \\int_{-2}^{1}\\int_{x^2}^{2-x}(x+y)\\,dy\\,dx\\]

  <p>Tích phân trong:</p>
  \\[\\int_{x^2}^{2-x}(x+y)\\,dy = \\left[xy+\\frac{y^2}{2}\\right]_{x^2}^{2-x}\\]
  \\[= x(2-x)+\\frac{(2-x)^2}{2} - x\\cdot x^2 - \\frac{x^4}{2}\\]
  \\[= 2x-x^2+\\frac{4-4x+x^2}{2}-x^3-\\frac{x^4}{2}\\]
  \\[= 2x-x^2+2-2x+\\frac{x^2}{2}-x^3-\\frac{x^4}{2}\\]
  \\[= 2-\\frac{x^2}{2}-x^3-\\frac{x^4}{2}\\]

  <p>Tích phân ngoài:</p>
  \\[I = \\int_{-2}^{1}\\left(2-\\frac{x^2}{2}-x^3-\\frac{x^4}{2}\\right)dx\\]
  \\[= \\left[2x-\\frac{x^3}{6}-\\frac{x^4}{4}-\\frac{x^5}{10}\\right]_{-2}^{1}\\]
  \\[= \\left(2-\\frac{1}{6}-\\frac{1}{4}-\\frac{1}{10}\\right)-\\left(-4+\\frac{8}{6}-4+\\frac{32}{10}\\right)\\]
  \\[= \\left(2-\\frac{1}{6}-\\frac{1}{4}-\\frac{1}{10}\\right)-\\left(-8+\\frac{4}{3}+\\frac{16}{5}\\right)\\]

  <p>Phần 1: mẫu chung 60: \\(2=\\frac{120}{60}\\), \\(\\frac{1}{6}=\\frac{10}{60}\\), \\(\\frac{1}{4}=\\frac{15}{60}\\), \\(\\frac{1}{10}=\\frac{6}{60}\\):<br>
  \\(= \\frac{120-10-15-6}{60} = \\frac{89}{60}\\)</p>

  <p>Phần 2: mẫu 15: \\(-8=\\frac{-120}{15}\\), \\(\\frac{4}{3}=\\frac{20}{15}\\), \\(\\frac{16}{5}=\\frac{48}{15}\\):<br>
  \\(= \\frac{-120+20+48}{15} = \\frac{-52}{15}\\)</p>

  \\[I = \\frac{89}{60} - \\frac{-52}{15} = \\frac{89}{60} + \\frac{208}{60} = \\frac{297}{60} = \\frac{99}{20}\\]

  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = \\dfrac{99}{20}}\\) ✓ Khớp với đáp án.</p>
</div>
""",

"B1_13": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B1.13</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D \\left(\\frac{x}{y}+\\frac{y}{x}\\right)dxdy\\), D là hình chữ nhật \\(1\\le x\\le 4\\), \\(1\\le y\\le 2\\).</p>

  <p><strong>Tính tích phân.</strong></p>
  \\[I = \\int_1^4\\int_1^2\\left(\\frac{x}{y}+\\frac{y}{x}\\right)dy\\,dx\\]

  <p>Tích phân trong theo \\(y\\):</p>
  \\[\\int_1^2\\left(\\frac{x}{y}+\\frac{y}{x}\\right)dy = \\left[x\\ln y + \\frac{y^2}{2x}\\right]_1^2 = x\\ln 2 + \\frac{4}{2x} - 0 - \\frac{1}{2x} = x\\ln 2 + \\frac{3}{2x}\\]

  <p>Tích phân ngoài theo \\(x\\):</p>
  \\[I = \\int_1^4\\left(x\\ln 2 + \\frac{3}{2x}\\right)dx = \\left[\\frac{x^2}{2}\\ln 2 + \\frac{3}{2}\\ln x\\right]_1^4\\]
  \\[= \\left(8\\ln 2 + \\frac{3}{2}\\ln 4\\right) - \\left(\\frac{1}{2}\\ln 2 + 0\\right)\\]
  \\[= 8\\ln 2 + \\frac{3}{2}\\cdot 2\\ln 2 - \\frac{1}{2}\\ln 2\\]
  \\[= 8\\ln 2 + 3\\ln 2 - \\frac{1}{2}\\ln 2 = \\frac{21}{2}\\ln 2\\]

  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = \\dfrac{21}{2}\\ln 2}\\) ✓ Khớp với đáp án \\(21\\ln(2)/2\\).</p>
</div>
""",

"B1_14": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B1.14</h3>
  <p><strong>Đề bài:</strong> Đổi thứ tự tích phân \\(\\displaystyle\\int_0^2 dx\\int_0^{\\sqrt{2x-x^2}} f(x,y)\\,dy\\).</p>

  <p><strong>Bước 1: Xác định miền D.</strong><br>
  Điều kiện: \\(0 \\le x \\le 2\\), \\(0 \\le y \\le \\sqrt{2x-x^2}\\).<br>
  Đường trên: \\(y = \\sqrt{2x-x^2}\\) tức \\(y^2 = 2x-x^2\\), hay \\((x-1)^2+y^2=1\\).<br>
  Đây là nửa trên (\\(y\\ge 0\\)) của đường tròn tâm \\((1,0)\\), bán kính \\(1\\).</p>

  <p><strong>Bước 2: Đổi thứ tự.</strong><br>
  \\(y\\) chạy từ \\(0\\) đến \\(1\\). Với \\(y\\) cố định, từ \\((x-1)^2 = 1-y^2\\):<br>
  \\(x = 1 \\pm \\sqrt{1-y^2}\\).<br>
  Vì \\(x\\ge 0\\), \\(x\\) chạy từ \\(1-\\sqrt{1-y^2}\\) đến \\(1+\\sqrt{1-y^2}\\).</p>

  \\[\\int_0^1 dy\\int_{1-\\sqrt{1-y^2}}^{1+\\sqrt{1-y^2}} f(x,y)\\,dx\\]

  <p style="color:#1a5276; font-weight:bold;">Đây là kết quả sau khi đổi thứ tự tích phân.</p>
</div>
""",

"B1_15": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B1.15</h3>
  <p><strong>Đề bài:</strong> Đổi thứ tự tích phân \\(\\displaystyle\\int_0^2 dx\\int_{\\sqrt{2x-x^2}}^{\\sqrt{2x}} f(x,y)\\,dy\\).</p>

  <p><strong>Bước 1: Xác định miền D.</strong><br>
  Điều kiện: \\(0\\le x\\le 2\\), \\(\\sqrt{2x-x^2} \\le y \\le \\sqrt{2x}\\).<br>
  — Đường dưới: \\(y = \\sqrt{2x-x^2}\\), tức \\((x-1)^2+y^2=1\\) (nửa trên đường tròn bán kính 1, tâm (1,0)).<br>
  — Đường trên: \\(y = \\sqrt{2x}\\), tức \\(y^2=2x\\) (parabol).</p>

  <p><strong>Bước 2: Phân tích theo chiều y.</strong><br>
  Giao điểm: \\(2x-x^2 = 2x \\Rightarrow x^2=0 \\Rightarrow x=0,y=0\\).<br>
  Giao điểm bên kia: \\(y^2=2x\\) và \\((x-1)^2+y^2=1\\): thay \\(y^2=2x\\):<br>
  \\((x-1)^2+2x=1 \\Rightarrow x^2-2x+1+2x=1 \\Rightarrow x^2=0 \\Rightarrow x=0\\).<br>
  Vậy chỉ giao tại \\((0,0)\\).<br>
  Khi \\(x=2\\): đường tròn cho \\(y=0\\), parabol cho \\(y=2\\). Miền D là vùng nằm ngoài đường tròn và dưới parabol.</p>

  <p><strong>Đổi thứ tự theo y:</strong><br>
  \\(y\\) từ \\(0\\) đến \\(2\\).<br>
  — Với \\(0\\le y\\le 1\\): trên đường tròn \\(x=1-\\sqrt{1-y^2}\\) hoặc \\(x=1+\\sqrt{1-y^2}\\). Phần bên ngoài đường tròn và dưới parabol: \\(0\\le x\\le 1-\\sqrt{1-y^2}\\) cộng \\(1+\\sqrt{1-y^2}\\le x\\le y^2/2\\).<br>
  — Với \\(1\\le y \\le 2\\): \\(0\\le x\\le y^2/2\\).</p>

  \\[\\int_0^1 dy\\left[\\int_0^{1-\\sqrt{1-y^2}}f\\,dx + \\int_{1+\\sqrt{1-y^2}}^{y^2/2}f\\,dx\\right] + \\int_1^2 dy\\int_0^{y^2/2}f\\,dx\\]

  <p style="color:#1a5276; font-weight:bold;">Đây là kết quả sau khi đổi thứ tự tích phân.</p>
</div>
""",

"B1_16": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B1.16</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D xy\\,dxdy\\), D là hình thang M(1,1), N(2,3), P(2,4), Q(1,5).</p>

  <p><strong>Bước 1: Tìm phương trình các cạnh.</strong><br>
  — MN: qua (1,1) và (2,3): hệ số góc \\(=\\frac{3-1}{2-1}=2\\), pt: \\(y=2x-1\\), tức \\(x=\\frac{y+1}{2}\\).<br>
  — QP: qua (1,5) và (2,4): hệ số góc \\(=\\frac{4-5}{2-1}=-1\\), pt: \\(y=-x+6\\), tức \\(x=6-y\\).<br>
  — MQ: \\(x=1\\) (cạnh trái).<br>
  — NP: \\(x=2\\) (cạnh phải).</p>

  <p><strong>Bước 2: Xác định giới hạn theo y.</strong><br>
  \\(y\\) từ 1 đến 5.<br>
  Điểm N và Q ứng với \\(x=2\\): N tại \\(y=3\\), Q tại \\(y=5\\); M tại \\(y=1\\), P tại \\(y=4\\).<br>
  — \\(1\\le y\\le 3\\): \\(x\\) từ \\(\\frac{y+1}{2}\\) (MN) đến \\(2\\) (NP).<br>
  — \\(3\\le y\\le 4\\): \\(x\\) từ \\(1\\) (MQ kéo dài?) ... Cần kiểm tra lại.<br>
  <em>Dùng thứ tự dx dy với x từ 1 đến 2:</em><br>
  Tại \\(x=1\\): \\(y\\) từ 1 (M) đến 5 (Q).<br>
  Tại \\(x=2\\): \\(y\\) từ 3 (N) đến 4 (P).<br>
  Tích phân theo x:</p>
  \\[I = \\int_1^2 x\\left(\\int_{y_{\\min}(x)}^{y_{\\max}(x)} y\\,dy\\right)dx\\]
  <p>Với \\(x\\) từ 1 đến 2: \\(y_{\\min}=2x-1\\) (MN) và \\(y_{\\max}=-x+6\\) (QP).</p>
  \\[I = \\int_1^2 x\\cdot\\frac{(-x+6)^2-(2x-1)^2}{2}\\,dx\\]
  \\[= \\frac{1}{2}\\int_1^2 x\\left[(x^2-12x+36)-(4x^2-4x+1)\\right]dx\\]
  \\[= \\frac{1}{2}\\int_1^2 x(-3x^2-8x+35)\\,dx = \\frac{1}{2}\\int_1^2(-3x^3-8x^2+35x)\\,dx\\]
  \\[= \\frac{1}{2}\\left[-\\frac{3x^4}{4}-\\frac{8x^3}{3}+\\frac{35x^2}{2}\\right]_1^2\\]
  \\[= \\frac{1}{2}\\left[\\left(-12-\\frac{64}{3}+70\\right)-\\left(-\\frac{3}{4}-\\frac{8}{3}+\\frac{35}{2}\\right)\\right]\\]
  \\[= \\frac{1}{2}\\left[\\left(58-\\frac{64}{3}\\right)-\\left(\\frac{35}{2}-\\frac{3}{4}-\\frac{8}{3}\\right)\\right]\\]

  <p>Phần 1 (mẫu 3): \\(58-\\frac{64}{3}=\\frac{174-64}{3}=\\frac{110}{3}\\).<br>
  Phần 2 (mẫu 12): \\(\\frac{35}{2}-\\frac{3}{4}-\\frac{8}{3}=\\frac{210-9-32}{12}=\\frac{169}{12}\\).</p>
  \\[I = \\frac{1}{2}\\left(\\frac{110}{3}-\\frac{169}{12}\\right) = \\frac{1}{2}\\cdot\\frac{440-169}{12} = \\frac{271}{24}\\]

  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = \\dfrac{271}{24}}\\) ✓ Khớp với đáp án.</p>
</div>
""",

"B1_17": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B1.17</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D x^4 y^4\\,dxdy\\), D giới hạn bởi \\(x=-y^2\\) và \\(y=x^2\\).</p>

  <p><strong>Bước 1: Tìm giao điểm.</strong><br>
  \\(x = -y^2\\) và \\(y = x^2\\): thay \\(x=-y^2\\) vào \\(y=x^2\\): \\(y=y^4 \\Rightarrow y(y^3-1)=0 \\Rightarrow y=0\\) hoặc \\(y=1\\).<br>
  Tại \\(y=0\\): \\(x=0\\). Tại \\(y=1\\): \\(x=-1\\).<br>
  Giao điểm: \\((0,0)\\) và \\((-1,1)\\).</p>

  <p><strong>Bước 2: Lấy y từ 0 đến 1, x từ \\(-y^2\\) đến \\(-\\sqrt{y}\\) (cần kiểm tra thứ tự).</strong><br>
  Trên D: \\(x=-y^2\\) là cạnh phải (\\(x\\) lớn hơn), \\(x=-\\sqrt{y}\\) từ \\(y=x^2\\Rightarrow x=-\\sqrt{y}\\) (phía âm).<br>
  So sánh: tại \\(y=1/4\\), \\(-y^2=-1/16\\) và \\(-\\sqrt{y}=-1/2\\). Ta thấy \\(-y^2 > -\\sqrt{y}\\), nên x từ \\(-\\sqrt{y}\\) đến \\(-y^2\\).</p>

  \\[I = \\int_0^1\\int_{-\\sqrt{y}}^{-y^2} x^4 y^4\\,dx\\,dy = \\int_0^1 y^4\\left[\\frac{x^5}{5}\\right]_{-\\sqrt{y}}^{-y^2}dy\\]
  \\[= \\frac{1}{5}\\int_0^1 y^4\\left[(-y^2)^5-(-\\sqrt{y})^5\\right]dy = \\frac{1}{5}\\int_0^1 y^4\\left[-y^{10}+y^{5/2}\\right]dy\\]
  \\[= \\frac{1}{5}\\int_0^1\\left(y^{13/2}-y^{14}\\right)dy\\]
  \\[= \\frac{1}{5}\\left[\\frac{y^{15/2}}{15/2}-\\frac{y^{15}}{15}\\right]_0^1 = \\frac{1}{5}\\left(\\frac{2}{15}-\\frac{1}{15}\\right) = \\frac{1}{5}\\cdot\\frac{1}{15} = \\frac{1}{75}\\]

  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = \\dfrac{1}{75}}\\) ✓ Khớp với đáp án.</p>
</div>
""",

"B1_18": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B1.18</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D xy\\,dxdy\\), D giới hạn bởi \\(y=1\\), \\(y=4\\), \\(xy=1\\), \\(x=0\\).</p>

  <p><strong>Bước 1: Xác định miền D.</strong><br>
  \\(xy=1 \\Rightarrow x=1/y\\). Với \\(1\\le y\\le 4\\), \\(x\\) từ \\(0\\) đến \\(1/y\\).</p>

  <p><strong>Bước 2: Tính tích phân.</strong></p>
  \\[I = \\int_1^4\\int_0^{1/y} xy\\,dx\\,dy = \\int_1^4 y\\cdot\\left[\\frac{x^2}{2}\\right]_0^{1/y}dy = \\int_1^4 y\\cdot\\frac{1}{2y^2}\\,dy = \\frac{1}{2}\\int_1^4 \\frac{1}{y}\\,dy\\]
  \\[= \\frac{1}{2}\\left[\\ln y\\right]_1^4 = \\frac{1}{2}\\ln 4 = \\frac{1}{2}\\cdot 2\\ln 2 = \\ln 2\\]

  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = \\ln 2}\\) ✓ Khớp với đáp án \\(\\ln(2)\\).</p>
</div>
""",

"B1_19": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B1.19</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D \\sqrt{|x^2-y|}\\,dxdy\\), D là hình chữ nhật \\(-1\\le x\\le 1\\), \\(0\\le y\\le 2\\).</p>

  <p><strong>Bước 1: Phân vùng theo dấu của \\(x^2-y\\).</strong><br>
  \\(x^2-y=0 \\Leftrightarrow y=x^2\\) (parabol).<br>
  — Vùng \\(D_1\\): \\(y < x^2\\) → \\(\\sqrt{x^2-y}\\).<br>
  — Vùng \\(D_2\\): \\(y > x^2\\) → \\(\\sqrt{y-x^2}\\).</p>

  <p><strong>Bước 2: Lợi dụng tính chẵn của \\(x\\).</strong></p>
  \\[I = 2\\int_0^1\\left[\\int_0^{x^2}\\sqrt{x^2-y}\\,dy + \\int_{x^2}^2\\sqrt{y-x^2}\\,dy\\right]dx\\]

  <p>Tích phân con 1 (đặt \\(u=x^2-y\\), \\(du=-dy\\)):</p>
  \\[\\int_0^{x^2}\\sqrt{x^2-y}\\,dy = \\left[-\\frac{2}{3}(x^2-y)^{3/2}\\right]_0^{x^2} = \\frac{2}{3}x^3\\]

  <p>Tích phân con 2 (đặt \\(u=y-x^2\\)):</p>
  \\[\\int_{x^2}^2\\sqrt{y-x^2}\\,dy = \\left[\\frac{2}{3}(y-x^2)^{3/2}\\right]_{x^2}^2 = \\frac{2}{3}(2-x^2)^{3/2}\\]

  \\[I = 2\\int_0^1\\left[\\frac{2}{3}x^3+\\frac{2}{3}(2-x^2)^{3/2}\\right]dx\\]
  \\[= \\frac{4}{3}\\int_0^1 x^3\\,dx + \\frac{4}{3}\\int_0^1(2-x^2)^{3/2}\\,dx\\]

  <p>Phần 1: \\(\\frac{4}{3}\\cdot\\frac{1}{4}=\\frac{1}{3}\\).</p>

  <p>Phần 2: đặt \\(x=\\sqrt{2}\\sin t\\), \\(dx=\\sqrt{2}\\cos t\\,dt\\), khi \\(x=0\\to t=0\\), \\(x=1\\to t=\\arcsin(1/\\sqrt{2})=\\pi/4\\):<br>
  \\((2-x^2)^{3/2} = (2\\cos^2 t)^{3/2} = 2\\sqrt{2}\\cos^3 t\\)</p>
  \\[\\int_0^1(2-x^2)^{3/2}dx = \\int_0^{\\pi/4}2\\sqrt{2}\\cos^3 t\\cdot\\sqrt{2}\\cos t\\,dt = 4\\int_0^{\\pi/4}\\cos^4 t\\,dt\\]

  <p>Dùng công thức: \\(\\cos^4 t = \\frac{3+4\\cos 2t+\\cos 4t}{8}\\):</p>
  \\[4\\int_0^{\\pi/4}\\cos^4 t\\,dt = 4\\left[\\frac{3t}{8}+\\frac{\\sin 2t}{4}+\\frac{\\sin 4t}{32}\\right]_0^{\\pi/4}\\]
  \\[= 4\\left(\\frac{3\\pi}{32}+\\frac{1}{4}+0\\right) = \\frac{3\\pi}{8}+1\\]

  \\[I = \\frac{1}{3}+\\frac{4}{3}\\left(\\frac{3\\pi}{8}+1\\right) = \\frac{1}{3}+\\frac{\\pi}{2}+\\frac{4}{3} = \\frac{5}{3}+\\frac{\\pi}{2}\\]

  <p>Số thập phân: \\(\\frac{5}{3}+\\frac{\\pi}{2} \\approx 1.667+1.571 = 3.238\\).</p>

  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = \\dfrac{5}{3}+\\dfrac{\\pi}{2} \\approx 3.238}\\) ✓ Khớp với đáp án \\(5/3+\\pi/2\\).</p>
</div>
""",

"B1_20": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B1.20</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D \\max(x^2,y)\\,dxdy\\), D giới hạn bởi \\(y=8-x^2\\) và trục \\(Ox\\).</p>

  <p><strong>Bước 1: Xác định miền D.</strong><br>
  \\(y=8-x^2=0 \\Rightarrow x=\\pm 2\\sqrt{2}\\).<br>
  D: \\(-2\\sqrt{2}\\le x\\le 2\\sqrt{2}\\), \\(0\\le y\\le 8-x^2\\).</p>

  <p><strong>Bước 2: Phân vùng max.</strong><br>
  \\(\\max(x^2,y) = x^2\\) khi \\(y\\le x^2\\), và \\(=y\\) khi \\(y\\ge x^2\\).<br>
  Đường biên \\(y=x^2\\) trong D.<br>
  — Vùng \\(D_1\\): \\(0\\le y\\le x^2\\): \\(\\max=x^2\\).<br>
  — Vùng \\(D_2\\): \\(x^2\\le y\\le 8-x^2\\): \\(\\max=y\\). Yêu cầu \\(x^2\\le 8-x^2 \\Rightarrow x^2\\le 4 \\Rightarrow |x|\\le 2\\).</p>

  <p><strong>Tính theo đối xứng (nhân 2 do tính chẵn):</strong></p>
  \\[I = 2\\left[\\int_0^{2\\sqrt{2}}\\int_0^{\\min(x^2,\\,8-x^2)} x^2\\,dy\\,dx + \\int_0^2\\int_{x^2}^{8-x^2} y\\,dy\\,dx + \\int_2^{2\\sqrt{2}}\\int_0^{8-x^2} x^2\\,dy\\,dx\\right]\\]

  <p>Với \\(x\\in[0,2]\\): \\(x^2\\le 4 = 8-x^2\\big|_{x=2}\\), nên đường \\(y=x^2\\) nằm dưới đường \\(y=8-x^2\\).</p>

  <p>Phần A: \\(\\int_0^2 x^2\\cdot x^2\\,dx=\\int_0^2 x^4\\,dx=\\frac{32}{5}\\).</p>
  <p>Phần B: \\(\\int_0^2\\frac{(8-x^2)^2-x^4}{2}\\,dx = \\frac{1}{2}\\int_0^2(64-16x^2+x^4-x^4)\\,dx = \\frac{1}{2}\\int_0^2(64-16x^2)\\,dx\\)<br>
  \\(= \\frac{1}{2}\\left[64x-\\frac{16x^3}{3}\\right]_0^2 = \\frac{1}{2}\\left(128-\\frac{128}{3}\\right)=\\frac{1}{2}\\cdot\\frac{256}{3}=\\frac{128}{3}\\).</p>
  <p>Phần C: \\(\\int_2^{2\\sqrt{2}} x^2(8-x^2)\\,dx = \\int_2^{2\\sqrt{2}}(8x^2-x^4)\\,dx\\)<br>
  \\(=\\left[\\frac{8x^3}{3}-\\frac{x^5}{5}\\right]_2^{2\\sqrt{2}}\\)<br>
  Tại \\(x=2\\sqrt{2}\\): \\(x^3=16\\sqrt{2}\\), \\(x^5=128\\sqrt{2}\\).<br>
  \\(=\\left(\\frac{128\\sqrt{2}}{3}-\\frac{128\\sqrt{2}}{5}\\right)-\\left(\\frac{64}{3}-\\frac{32}{5}\\right)\\)<br>
  \\(=128\\sqrt{2}\\left(\\frac{1}{3}-\\frac{1}{5}\\right)-\\frac{2(160-48)}{15}=128\\sqrt{2}\\cdot\\frac{2}{15}-\\frac{224}{15}\\)<br>
  \\(=\\frac{256\\sqrt{2}}{15}-\\frac{224}{15}\\).</p>

  \\[I = 2\\left(\\frac{32}{5}+\\frac{128}{3}+\\frac{256\\sqrt{2}}{15}-\\frac{224}{15}\\right)\\]
  \\[= 2\\left(\\frac{96}{15}+\\frac{640}{15}+\\frac{256\\sqrt{2}}{15}-\\frac{224}{15}\\right)\\]
  \\[= 2\\cdot\\frac{512+256\\sqrt{2}}{15} = \\frac{1024+512\\sqrt{2}}{15} = \\frac{1024}{15}+\\frac{512\\sqrt{2}}{15}\\]

  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = \\dfrac{1024}{15}+\\dfrac{512\\sqrt{2}}{15}}\\) ✓ Khớp với đáp án.</p>
</div>
""",

}

def add_solution_to_file(filename, solution_html):
    filepath = os.path.join(BASE_DIR, filename + ".html")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Kiểm tra xem đã có lời giải chưa
    if 'Lời giải' in content or 'border-left:5px solid #2980b9' in content:
        print(f"  [BỎ QUA] {filename}.html - đã có lời giải")
        return False
    
    # Chèn lời giải trước </div>\n</body>
    insert_before = '</div>\n</body>'
    if insert_before not in content:
        insert_before = '</div>\r\n</body>'
    if insert_before not in content:
        # Thử tìm </body>
        insert_before = '</body>'
    
    new_content = content.replace(insert_before, solution_html + '\n' + insert_before, 1)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"  [OK] Đã thêm lời giải vào {filename}.html")
    return True

if __name__ == "__main__":
    print("=== Thêm lời giải vào các file B1 ===\n")
    count = 0
    for key, sol in solutions.items():
        result = add_solution_to_file(key, sol)
        if result:
            count += 1
    print(f"\nHoàn thành! Đã thêm lời giải cho {count}/{len(solutions)} bài.")
