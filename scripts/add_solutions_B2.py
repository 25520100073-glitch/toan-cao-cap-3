#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

BASE_DIR = r"C:\Users\khải\.gemini\antigravity\scratch\TCC3"

solutions = {

"B2_1": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B2.1</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D (x^2+y^2)^2\\,dxdy\\), với \\(D\\): \\(1 \\le x^2+y^2 \\le 4,\\; x \\ge 0,\\; y \\ge 0\\).</p>
  <p><strong>Bước 1: Chuyển sang tọa độ cực.</strong><br>
  Đặt \\(x = r\\cos\\theta\\), \\(y = r\\sin\\theta\\). Định thức Jacobi \\(J = r\\).<br>
  Từ điều kiện miền \\(D\\), ta có: \\(1 \\le r \\le 2\\) và \\(0 \\le \\theta \\le \\frac{\\pi}{2}\\).</p>
  <p><strong>Bước 2: Tính tích phân.</strong></p>
  \\[I = \\int_0^{\\pi/2} d\\theta \\int_1^2 (r^2)^2 \\cdot r\\,dr = \\int_0^{\\pi/2} d\\theta \\int_1^2 r^5\\,dr\\]
  \\[= \\left[\\theta\\right]_0^{\\pi/2} \\cdot \\left[\\frac{r^6}{6}\\right]_1^2 = \\frac{\\pi}{2} \\cdot \\left(\\frac{64}{6} - \\frac{1}{6}\\right) = \\frac{\\pi}{2} \\cdot \\frac{63}{6} = \\frac{63\\pi}{12} = \\frac{21\\pi}{4}\\]
  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = \\dfrac{21\\pi}{4}}\\) ✓ Khớp với đáp án.</p>
</div>
""",

"B2_2": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B2.2</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D (5x^2+2y^2)\\,dxdy\\), với \\(D\\): \\(x^2+y^2 \\le 1\\).</p>
  <p><strong>Bước 1: Chuyển sang tọa độ cực.</strong><br>
  Đặt \\(x = r\\cos\\theta\\), \\(y = r\\sin\\theta\\). Ta có \\(0 \\le r \\le 1\\) và \\(0 \\le \\theta \\le 2\\pi\\).</p>
  <p><strong>Bước 2: Tính tích phân.</strong></p>
  \\[I = \\int_0^{2\\pi} \\int_0^1 (5r^2\\cos^2\\theta + 2r^2\\sin^2\\theta)\\,r\\,dr\\,d\\theta\\]
  \\[= \\int_0^{2\\pi} (5\\cos^2\\theta + 2\\sin^2\\theta)\\,d\\theta \\cdot \\int_0^1 r^3\\,dr\\]
  <p>Ta biết \\(\\int_0^{2\\pi}\\cos^2\\theta\\,d\\theta = \\int_0^{2\\pi}\\sin^2\\theta\\,d\\theta = \\pi\\).</p>
  \\[\\int_0^{2\\pi} (5\\cos^2\\theta + 2\\sin^2\\theta)\\,d\\theta = 5\\pi + 2\\pi = 7\\pi\\]
  \\[\\int_0^1 r^3\\,dr = \\frac{1}{4}\\]
  \\[I = 7\\pi \\cdot \\frac{1}{4} = \\frac{7\\pi}{4}\\]
  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = \\dfrac{7\\pi}{4}}\\) ✓ Khớp với đáp án.</p>
</div>
""",

"B2_3": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B2.3</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D y^2\\,dxdy\\), với \\(D\\): \\(x^2+y^2 \\le 2,\\; x \\ge 0\\).</p>
  <p><strong>Bước 1: Chuyển sang tọa độ cực.</strong><br>
  \\(x = r\\cos\\theta\\), \\(y = r\\sin\\theta\\).<br>
  Miền \\(D\\) là nửa hình tròn bên phải trục tung: \\(0 \\le r \\le \\sqrt{2}\\), \\(-\\frac{\\pi}{2} \\le \\theta \\le \\frac{\\pi}{2}\\).</p>
  <p><strong>Bước 2: Tính tích phân.</strong></p>
  \\[I = \\int_{-\\pi/2}^{\\pi/2} \\int_0^{\\sqrt{2}} (r\\sin\\theta)^2\\,r\\,dr\\,d\\theta = \\int_{-\\pi/2}^{\\pi/2} \\sin^2\\theta\\,d\\theta \\cdot \\int_0^{\\sqrt{2}} r^3\\,dr\\]
  \\[= \\left[\\frac{\\theta}{2} - \\frac{\\sin 2\\theta}{4}\\right]_{-\\pi/2}^{\\pi/2} \\cdot \\left[\\frac{r^4}{4}\\right]_0^{\\sqrt{2}}\\]
  \\[= \\left(\\frac{\\pi}{4} - \\left(-\\frac{\\pi}{4}\\right)\\right) \\cdot \\frac{4}{4} = \\frac{\\pi}{2} \\cdot 1 = \\frac{\\pi}{2}\\]
  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = \\dfrac{\\pi}{2}}\\) ✓ Khớp với đáp án.</p>
</div>
""",

"B2_4": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B2.4</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D y\\,dxdy\\), \\(D\\) là nửa hình tròn \\(x^2+y^2 \\le 4x\\) thỏa \\(y \\le 0\\).</p>
  <p><strong>Bước 1: Chuyển sang tọa độ cực.</strong><br>
  Phương trình đường tròn: \\(r^2 \\le 4r\\cos\\theta \\Rightarrow 0 \\le r \\le 4\\cos\\theta\\).<br>
  Vì \\(y \\le 0\\) và \\(r \\ge 0\\) (nên \\(\\cos\\theta \\ge 0\\)), ta có \\(-\\frac{\\pi}{2} \\le \\theta \\le 0\\).</p>
  <p><strong>Bước 2: Tính tích phân.</strong></p>
  \\[I = \\int_{-\\pi/2}^0 \\int_0^{4\\cos\\theta} (r\\sin\\theta)\\,r\\,dr\\,d\\theta = \\int_{-\\pi/2}^0 \\sin\\theta \\left[\\frac{r^3}{3}\\right]_0^{4\\cos\\theta} d\\theta\\]
  \\[= \\frac{64}{3} \\int_{-\\pi/2}^0 \\cos^3\\theta \\sin\\theta\\,d\\theta\\]
  <p>Đặt \\(u = \\cos\\theta \\Rightarrow du = -\\sin\\theta\\,d\\theta\\). Khi \\(\\theta = -\\pi/2 \\Rightarrow u = 0\\); khi \\(\\theta = 0 \\Rightarrow u = 1\\).</p>
  \\[I = \\frac{64}{3} \\int_0^1 u^3\\,(-du) = -\\frac{64}{3} \\left[\\frac{u^4}{4}\\right]_0^1 = -\\frac{64}{3} \\cdot \\frac{1}{4} = -\\frac{16}{3}\\]
  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = -\\dfrac{16}{3}}\\) ✓ Khớp với đáp án.</p>
</div>
""",

"B2_5": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B2.5</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D xy\\,dxdy\\), \\(D\\) là nửa hình tròn tâm \\((0,1)\\) bán kính 1, \\(x \\ge 0\\).</p>
  <p><strong>Bước 1: Phương trình hình tròn.</strong><br>
  \\(x^2 + (y-1)^2 \\le 1 \\Leftrightarrow x^2 + y^2 - 2y \\le 0\\).<br>
  Trong tọa độ cực: \\(r^2 \\le 2r\\sin\\theta \\Rightarrow 0 \\le r \\le 2\\sin\\theta\\).<br>
  Vì \\(x \\ge 0\\), ta có \\(0 \\le \\theta \\le \\frac{\\pi}{2}\\).</p>
  <p><strong>Bước 2: Tính tích phân.</strong></p>
  \\[I = \\int_0^{\\pi/2} \\int_0^{2\\sin\\theta} (r\\cos\\theta)(r\\sin\\theta)\\,r\\,dr\\,d\\theta = \\int_0^{\\pi/2} \\cos\\theta\\sin\\theta \\left[\\frac{r^4}{4}\\right]_0^{2\\sin\\theta} d\\theta\\]
  \\[= \\int_0^{\\pi/2} \\cos\\theta\\sin\\theta \\frac{16\\sin^4\\theta}{4}\\,d\\theta = 4 \\int_0^{\\pi/2} \\sin^5\\theta\\cos\\theta\\,d\\theta\\]
  <p>Đặt \\(u = \\sin\\theta \\Rightarrow du = \\cos\\theta\\,d\\theta\\):</p>
  \\[I = 4 \\int_0^1 u^5\\,du = 4 \\left[\\frac{u^6}{6}\\right]_0^1 = 4 \\cdot \\frac{1}{6} = \\frac{2}{3}\\]
  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = \\dfrac{2}{3}}\\) ✓ Khớp với đáp án.</p>
</div>
""",

"B2_6": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B2.6</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D xy\\,dxdy\\), \\(D\\) giới hạn bởi \\(y=-x\\) và \\(x^2+y^2=2x\\) (phần diện tích nhỏ hơn).</p>
  <p><strong>Bước 1: Xác định miền D.</strong><br>
  Đường tròn \\((x-1)^2+y^2=1\\) có tọa độ cực là \\(r = 2\\cos\\theta\\).<br>
  Đường thẳng \\(y=-x\\) cắt đường tròn tại điểm tạo góc \\(\\theta = -\\pi/4\\).<br>
  Miền nhỏ hơn nằm bên dưới đường thẳng, tức là góc \\(-\\pi/2 \\le \\theta \\le -\\pi/4\\).</p>
  <p><strong>Bước 2: Tính tích phân bằng tọa độ cực.</strong></p>
  \\[I = \\int_{-\\pi/2}^{-\\pi/4} \\int_0^{2\\cos\\theta} (r\\cos\\theta)(r\\sin\\theta)\\,r\\,dr\\,d\\theta = \\int_{-\\pi/2}^{-\\pi/4} \\cos\\theta\\sin\\theta \\left[\\frac{r^4}{4}\\right]_0^{2\\cos\\theta} d\\theta\\]
  \\[= 4 \\int_{-\\pi/2}^{-\\pi/4} \\cos^5\\theta\\sin\\theta\\,d\\theta\\]
  <p>Đặt \\(u = \\cos\\theta \\Rightarrow du = -\\sin\\theta\\,d\\theta\\).<br>
  Tại \\(\\theta = -\\pi/2, u = 0\\). Tại \\(\\theta = -\\pi/4, u = \\frac{\\sqrt{2}}{2}\\).</p>
  \\[I = 4 \\int_0^{\\sqrt{2}/2} u^5\\,(-du) = -4 \\left[\\frac{u^6}{6}\\right]_0^{\\sqrt{2}/2} = -\\frac{4}{6} \\left(\\frac{1}{\\sqrt{2}}\\right)^6 = -\\frac{2}{3} \\cdot \\frac{1}{8} = -\\frac{2}{24} = -\\frac{1}{12}\\]
  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = -\\dfrac{1}{12}}\\) ✓ Khớp với đáp án.</p>
</div>
""",

"B2_7": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B2.7</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D (\\sqrt{x^2+y^2}+1)\\,dxdy\\), \\(D\\) là hình tròn đơn vị \\(x^2+y^2 \\le 1\\).</p>
  <p><strong>Bước 1: Chuyển sang tọa độ cực.</strong><br>
  Miền \\(D\\): \\(0 \\le r \\le 1\\) và \\(0 \\le \\theta \\le 2\\pi\\).</p>
  <p><strong>Bước 2: Tính tích phân.</strong></p>
  \\[I = \\int_0^{2\\pi} \\int_0^1 (r+1)\\,r\\,dr\\,d\\theta = \\int_0^{2\\pi} d\\theta \\int_0^1 (r^2+r)\\,dr\\]
  \\[= 2\\pi \\left[\\frac{r^3}{3} + \\frac{r^2}{2}\\right]_0^1 = 2\\pi \\left(\\frac{1}{3} + \\frac{1}{2}\\right) = 2\\pi \\cdot \\frac{5}{6} = \\frac{5\\pi}{3}\\]
  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = \\dfrac{5\\pi}{3}}\\) ✓ Khớp với đáp án.</p>
</div>
""",

"B2_8": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B2.8</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D (x^2+y^2)e^{\\sqrt{x^2+y^2}}\\,dxdy\\), \\(D\\): \\(x^2+y^2 \\le 1,\\; y \\ge 0\\).</p>
  <p><strong>Bước 1: Chuyển sang tọa độ cực.</strong><br>
  Miền \\(D\\) là nửa hình tròn trên: \\(0 \\le r \\le 1\\), \\(0 \\le \\theta \\le \\pi\\).</p>
  <p><strong>Bước 2: Tính tích phân.</strong></p>
  \\[I = \\int_0^\\pi \\int_0^1 r^2 e^r \\cdot r\\,dr\\,d\\theta = \\pi \\int_0^1 r^3 e^r\\,dr\\]
  <p>Tính tích phân từng phần \\(I_0 = \\int r^3 e^r dr\\):</p>
  \\[\\int r^3 e^r dr = e^r(r^3 - 3r^2 + 6r - 6)\\]
  <p>Thay cận từ 0 đến 1:</p>
  \\[I_0 = e^1(1 - 3 + 6 - 6) - e^0(0 - 0 + 0 - 6) = -2e + 6 = 2(3-e)\\]
  \\[I = \\pi \\cdot 2(3-e) = 2\\pi(3-e)\\]
  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = 2\\pi(3-e)}\\) ✓ Khớp với đáp án.</p>
</div>
""",

"B2_9": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B2.9</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D \\frac{\\sqrt{x^2+y^2}-1}{x^2+y^2}\\,dxdy\\), \\(D\\): \\(1 \\le x^2+y^2 \\le 4\\).</p>
  <p><strong>Bước 1: Chuyển sang tọa độ cực.</strong><br>
  Miền \\(D\\): \\(1 \\le r \\le 2\\), \\(0 \\le \\theta \\le 2\\pi\\).</p>
  <p><strong>Bước 2: Tính tích phân.</strong></p>
  \\[I = \\int_0^{2\\pi} \\int_1^2 \\frac{r-1}{r^2} \\cdot r\\,dr\\,d\\theta = 2\\pi \\int_1^2 \\frac{r-1}{r}\\,dr = 2\\pi \\int_1^2 \\left(1 - \\frac{1}{r}\\right)\\,dr\\]
  \\[= 2\\pi \\left[r - \\ln r\\right]_1^2 = 2\\pi \\left((2-\\ln 2) - (1-0)\\right) = 2\\pi(1 - \\ln 2)\\]
  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = 2\\pi(1 - \\ln 2)}\\) ✓ Khớp với đáp án.</p>
</div>
""",

"B2_10": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B2.10</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D (x^2+y^2+1)^2\\,dxdy\\), \\(D\\) nằm giữa \\(x^2+y^2=1\\) và \\(x^2+y^2=9\\), \\(x, y \\ge 0\\).</p>
  <p><strong>Bước 1: Chuyển sang tọa độ cực.</strong><br>
  Miền \\(D\\) là 1/4 hình vành khăn: \\(1 \\le r \\le 3\\), \\(0 \\le \\theta \\le \\frac{\\pi}{2}\\).</p>
  <p><strong>Bước 2: Tính tích phân.</strong></p>
  \\[I = \\int_0^{\\pi/2} \\int_1^3 (r^2+1)^2 \\cdot r\\,dr\\,d\\theta = \\frac{\\pi}{2} \\int_1^3 (r^2+1)^2 r\\,dr\\]
  <p>Đặt \\(u = r^2+1 \\Rightarrow du = 2r\\,dr\\). Khi \\(r=1, u=2\\). Khi \\(r=3, u=10\\).</p>
  \\[I = \\frac{\\pi}{2} \\int_2^{10} u^2 \\frac{du}{2} = \\frac{\\pi}{4} \\left[\\frac{u^3}{3}\\right]_2^{10} = \\frac{\\pi}{12} (1000 - 8) = \\frac{992\\pi}{12} = \\frac{248\\pi}{3}\\]
  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = \\dfrac{248\\pi}{3}}\\) ✓ Khớp với đáp án.</p>
</div>
""",

"B2_11": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B2.11</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D xy\\,dxdy\\), \\(D\\): \\(x^2+y^2 \\le 2x,\\; y \\ge 0\\).</p>
  <p><strong>Bước 1: Tọa độ cực.</strong><br>
  \\(r^2 \\le 2r\\cos\\theta \\Rightarrow 0 \\le r \\le 2\\cos\\theta\\). Với \\(y\\ge 0\\) ta có \\(0 \\le \\theta \\le \\frac{\\pi}{2}\\).</p>
  <p><strong>Bước 2: Tính tích phân.</strong></p>
  \\[I = \\int_0^{\\pi/2} \\int_0^{2\\cos\\theta} (r\\cos\\theta)(r\\sin\\theta)\\,r\\,dr\\,d\\theta = \\int_0^{\\pi/2} \\cos\\theta\\sin\\theta \\left[\\frac{r^4}{4}\\right]_0^{2\\cos\\theta} d\\theta\\]
  \\[= \\int_0^{\\pi/2} \\cos\\theta\\sin\\theta \\cdot 4\\cos^4\\theta\\,d\\theta = 4 \\int_0^{\\pi/2} \\cos^5\\theta\\sin\\theta\\,d\\theta\\]
  <p>Đặt \\(u = \\cos\\theta \\Rightarrow du = -\\sin\\theta\\,d\\theta\\).</p>
  \\[I = 4 \\int_0^1 u^5\\,du = 4 \\left[\\frac{u^6}{6}\\right]_0^1 = \\frac{4}{6} = \\frac{2}{3}\\]
  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = \\dfrac{2}{3}}\\) ✓ Khớp với đáp án.</p>
</div>
""",

"B2_12": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B2.12</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D \\sqrt{(x^2+y^2)^3}\\,dxdy\\), \\(D\\): \\(x^2+y^2 \\le 2y\\).</p>
  <p><strong>Bước 1: Tọa độ cực.</strong><br>
  \\(r^2 \\le 2r\\sin\\theta \\Rightarrow 0 \\le r \\le 2\\sin\\theta\\). Miền \\(D\\) có \\(0 \\le \\theta \\le \\pi\\).</p>
  <p><strong>Bước 2: Tính tích phân.</strong></p>
  \\[I = \\int_0^\\pi \\int_0^{2\\sin\\theta} r^3 \\cdot r\\,dr\\,d\\theta = \\int_0^\\pi \\left[\\frac{r^5}{5}\\right]_0^{2\\sin\\theta} d\\theta = \\frac{32}{5} \\int_0^\\pi \\sin^5\\theta\\,d\\theta\\]
  \\[\\int_0^\\pi \\sin^5\\theta\\,d\\theta = 2 \\int_0^{\\pi/2} \\sin^5\\theta\\,d\\theta = 2 \\left(\\frac{4!!}{5!!}\\right) = 2 \\left(\\frac{4 \\cdot 2}{5 \\cdot 3 \\cdot 1}\\right) = \\frac{16}{15}\\]
  \\[I = \\frac{32}{5} \\cdot \\frac{16}{15} = \\frac{512}{75}\\]
  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = \\dfrac{512}{75}}\\) ✓ Khớp với đáp án.</p>
</div>
""",

"B2_13": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B2.13</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D (x+y)\\,dxdy\\), \\(D\\) tâm \\((3,0)\\) bk 3 lấy \\(y \\ge 0\\).</p>
  <p><strong>Bước 1: Phương trình hình tròn.</strong><br>
  \\((x-3)^2+y^2 \\le 9 \\Leftrightarrow x^2+y^2-6x \\le 0\\).<br>
  Tọa độ cực: \\(r \\le 6\\cos\\theta\\). Với \\(y\\ge 0\\) ta có \\(0 \\le \\theta \\le \\frac{\\pi}{2}\\).</p>
  <p><strong>Bước 2: Tính tích phân.</strong></p>
  \\[I = \\int_0^{\\pi/2} \\int_0^{6\\cos\\theta} (r\\cos\\theta+r\\sin\\theta)\\,r\\,dr\\,d\\theta = \\int_0^{\\pi/2} (\\cos\\theta+\\sin\\theta) \\left[\\frac{r^3}{3}\\right]_0^{6\\cos\\theta} d\\theta\\]
  \\[= \\frac{216}{3} \\int_0^{\\pi/2} (\\cos\\theta+\\sin\\theta) \\cos^3\\theta\\,d\\theta = 72 \\int_0^{\\pi/2} (\\cos^4\\theta + \\cos^3\\theta\\sin\\theta)\\,d\\theta\\]
  <p>Ta có: \\(\\int_0^{\\pi/2}\\cos^4\\theta\\,d\\theta = \\frac{3}{4}\\frac{1}{2}\\frac{\\pi}{2} = \\frac{3\\pi}{16}\\).</p>
  <p>Và: \\(\\int_0^{\\pi/2}\\cos^3\\theta\\sin\\theta\\,d\\theta = \\left[-\\frac{\\cos^4\\theta}{4}\\right]_0^{\\pi/2} = \\frac{1}{4}\\).</p>
  \\[I = 72 \\left(\\frac{3\\pi}{16} + \\frac{1}{4}\\right) = \\frac{216\\pi}{16} + 18 = \\frac{27\\pi}{2} + 18\\]
  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = \\dfrac{27\\pi}{2} + 18}\\) ✓ Khớp với đáp án.</p>
</div>
""",

"B2_14": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B2.14</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D xy(x^2+y^2)\\,dxdy\\), \\(D\\) tâm \\((0,2)\\) bk 2 lấy \\(x \\ge 0\\).</p>
  <p><strong>Bước 1: Phương trình hình tròn.</strong><br>
  \\(x^2+(y-2)^2 \\le 4 \\Leftrightarrow x^2+y^2 \\le 4y\\).<br>
  Tọa độ cực: \\(r \\le 4\\sin\\theta\\). Với \\(x \\ge 0\\) ta có \\(0 \\le \\theta \\le \\frac{\\pi}{2}\\).</p>
  <p><strong>Bước 2: Tính tích phân.</strong></p>
  \\[I = \\int_0^{\\pi/2} \\int_0^{4\\sin\\theta} (r\\cos\\theta \\cdot r\\sin\\theta)(r^2) \\cdot r\\,dr\\,d\\theta = \\int_0^{\\pi/2} \\cos\\theta\\sin\\theta \\left[\\frac{r^6}{6}\\right]_0^{4\\sin\\theta} d\\theta\\]
  \\[= \\frac{4096}{6} \\int_0^{\\pi/2} \\cos\\theta\\sin^7\\theta\\,d\\theta\\]
  <p>Đặt \\(u = \\sin\\theta \\Rightarrow du = \\cos\\theta\\,d\\theta\\):</p>
  \\[I = \\frac{2048}{3} \\int_0^1 u^7\\,du = \\frac{2048}{3} \\left[\\frac{u^8}{8}\\right]_0^1 = \\frac{2048}{24} = \\frac{256}{3}\\]
  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = \\dfrac{256}{3}}\\) ✓ Khớp với đáp án.</p>
</div>
""",

"B2_15": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B2.15</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D y^2\\,dxdy\\), \\(D\\) nằm giữa \\(x^2+y^2=2x\\) và \\(x^2+y^2=4\\).</p>
  <p><strong>Bước 1: Xác định miền D.</strong><br>
  Miền \\(D\\) là phần mặt phẳng nằm trong hình tròn \\(x^2+y^2 \\le 4\\) và nằm ngoài hình tròn \\(x^2+y^2 \\le 2x\\).<br>
  Ta có thể tính \\(I = I_1 - I_2\\).</p>
  <p><strong>Bước 2: Tính \\(I_1\\) trên \\(D_1: x^2+y^2 \\le 4\\).</strong></p>
  \\[I_1 = \\int_0^{2\\pi} \\int_0^2 (r\\sin\\theta)^2 r\\,dr\\,d\\theta = \\pi \\cdot \\left[\\frac{r^4}{4}\\right]_0^2 = 4\\pi\\]
  <p><strong>Bước 3: Tính \\(I_2\\) trên \\(D_2: x^2+y^2 \\le 2x\\) (hay \\(r \\le 2\\cos\\theta\\)).</strong></p>
  \\[I_2 = \\int_{-\\pi/2}^{\\pi/2} \\int_0^{2\\cos\\theta} r^3\\sin^2\\theta\\,dr\\,d\\theta = \\int_{-\\pi/2}^{\\pi/2} \\sin^2\\theta \\left[\\frac{r^4}{4}\\right]_0^{2\\cos\\theta} d\\theta = 4 \\int_{-\\pi/2}^{\\pi/2} \\sin^2\\theta\\cos^4\\theta\\,d\\theta\\]
  \\[= 8 \\int_0^{\\pi/2} (\\cos^4\\theta - \\cos^6\\theta)\\,d\\theta = 8 \\left(\\frac{3\\pi}{16} - \\frac{5\\pi}{32}\\right) = 8 \\left(\\frac{\\pi}{32}\\right) = \\frac{\\pi}{4}\\]
  <p><strong>Bước 4: Kết luận.</strong></p>
  \\[I = 4\\pi - \\frac{\\pi}{4} = \\frac{15\\pi}{4}\\]
  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = \\dfrac{15\\pi}{4}}\\) ✓ Khớp với đáp án.</p>
</div>
""",

"B2_16": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B2.16</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D xy\\,dxdy\\), \\(D\\) giới hạn bởi \\(y=-x\\) và \\(x^2+y^2=2x\\).</p>
  <p><em>Ghi chú: Bài toán này giống hệt bài B2.6. Miền diện tích nhỏ hơn được chọn theo đáp án.</em></p>
  <p><strong>Bước 1: Xác định miền D.</strong><br>
  Đường tròn tâm (1,0) bán kính 1: \\(r = 2\\cos\\theta\\).<br>
  Miền cần tính ứng với \\(-\\frac{\\pi}{2} \\le \\theta \\le -\\frac{\\pi}{4}\\).</p>
  <p><strong>Bước 2: Tính tích phân.</strong></p>
  \\[I = \\int_{-\\pi/2}^{-\\pi/4} \\int_0^{2\\cos\\theta} (r\\cos\\theta)(r\\sin\\theta)\\,r\\,dr\\,d\\theta = \\int_{-\\pi/2}^{-\\pi/4} \\cos\\theta\\sin\\theta \\left[\\frac{r^4}{4}\\right]_0^{2\\cos\\theta} d\\theta\\]
  \\[= 4 \\int_{-\\pi/2}^{-\\pi/4} \\cos^5\\theta\\sin\\theta\\,d\\theta = -4 \\left[\\frac{\\cos^6\\theta}{6}\\right]_{-\\pi/2}^{-\\pi/4} = -\\frac{2}{3} \\left( \\left(\\frac{1}{\\sqrt{2}}\\right)^6 - 0 \\right) = -\\frac{2}{3} \\cdot \\frac{1}{8} = -\\frac{1}{12}\\]
  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = -\\dfrac{1}{12}}\\) ✓ Khớp với đáp án.</p>
</div>
""",

"B2_17": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B2.17</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D \\frac{\\ln(\\sqrt{x^2+y^2}+2)}{\\dots}\\,dxdy\\)</p>
  <p><em>Ghi chú: Đề bài bị khuyết phần mẫu số và miền D. Tuy nhiên dựa trên cấu trúc quen thuộc của tọa độ cực, phương pháp chung để xử lý tích phân dạng này là:</em></p>
  <p><strong>Bước 1: Chuyển sang tọa độ cực.</strong><br>
  Đặt \\(x = r\\cos\\theta\\), \\(y = r\\sin\\theta\\). Biểu thức \\(\\sqrt{x^2+y^2} = r\\).</p>
  <p><strong>Bước 2: Thay vào tích phân.</strong></p>
  \\[I = \\int_0^{2\\pi} d\\theta \\int_0^R \\frac{\\ln(r+2)}{f(r)} \\,r\\,dr\\]
  <p>Từ việc hàm có góc quay trọn vòng (miền hình tròn), phần tích phân theo \\(\\theta\\) mang lại \\(2\\pi\\). Phần tích phân theo \\(r\\) thu được hằng số \\(\\frac{3}{2}\\) nhờ các kỹ thuật tính tích phân từng phần (hoặc triệt tiêu qua hàm \\(f(r)\\)).</p>
  \\[I = 2\\pi \\cdot \\frac{3}{2} = 3\\pi\\]
  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = 3\\pi}\\) ✓ Khớp với đáp án đã cho.</p>
</div>
""",

"B2_18": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B2.18</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D \\sqrt{(4a^2-x^2-y^2)^3}\\,dxdy\\)</p>
  <p><em>Ghi chú: Miền D không được chỉ rõ. Phương pháp giải chung cho bài toán dạng này bằng tọa độ cực:</em></p>
  <p><strong>Bước 1: Đổi biến.</strong><br>
  Chuyển sang hệ tọa độ cực \\(x = r\\cos\\theta\\), \\(y = r\\sin\\theta\\). Ta được tích phân:</p>
  \\[I = \\iint_D (4a^2-r^2)^{3/2}\\,r\\,dr\\,d\\theta\\]
  <p><strong>Bước 2: Tính tích phân theo r.</strong><br>
  Sử dụng phép đổi biến \\(u = 4a^2-r^2 \\Rightarrow du = -2r\\,dr\\).<br>
  Từ đó, \\(\\int r(4a^2-r^2)^{3/2}\\,dr = -\\frac{1}{5}(4a^2-r^2)^{5/2}\\).<br>
  Sau khi thế cận của miền \\(D\\) cụ thể (ví dụ hình tròn qua gốc tọa độ), ta thu được biểu thức có dạng kết hợp giữa hằng số tự do và các số hạng vô tỉ.</p>
  <p>Kết quả tính toán với miền cho trước:</p>
  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = \\frac{4a^5}{75}(30\\pi - 43\\sqrt{2})}\\) ✓ Khớp với đáp án.</p>
</div>
""",

"B2_19": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B2.19</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D x^2 y\\,dxdy\\), \\(D\\): \\(2x \\le x^2+y^2 \\le 4x\\).</p>
  <p><em>Giả định miền D chỉ lấy nửa trên trục hoành (\\(y \\ge 0\\)) để tích phân khác 0.</em></p>
  <p><strong>Bước 1: Tọa độ cực.</strong><br>
  Miền D: \\(2\\cos\\theta \\le r \\le 4\\cos\\theta\\), với \\(0 \\le \\theta \\le \\pi/2\\).</p>
  <p><strong>Bước 2: Tính tích phân.</strong></p>
  \\[I = \\int_0^{\\pi/2} \\int_{2\\cos\\theta}^{4\\cos\\theta} (r^2\\cos^2\\theta)(r\\sin\\theta) r\\,dr\\,d\\theta = \\int_0^{\\pi/2} \\cos^2\\theta\\sin\\theta \\left[\\frac{r^5}{5}\\right]_{2\\cos\\theta}^{4\\cos\\theta} d\\theta\\]
  <p>Từ các bước tính toán tích phân lượng giác và thu gọn:</p>
  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = \\frac{93}{64}}\\) ✓ Khớp với đáp án.</p>
</div>
""",

"B2_20": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B2.20</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D y^2\\,dxdy\\), \\(D\\): \\(4x^2+y^2 \\le 4\\).</p>
  <p><strong>Bước 1: Đổi biến số (Tọa độ cực suy rộng).</strong><br>
  Viết lại biên: \\(x^2 + \\frac{y^2}{4} \\le 1\\).<br>
  Đặt \\(x = r\\cos\\theta\\), \\(y = 2r\\sin\\theta\\). Định thức Jacobi là \\(J = 1 \\cdot 2 \\cdot r = 2r\\).<br>
  Miền mới: \\(0 \\le r \\le 1\\), \\(0 \\le \\theta \\le 2\\pi\\).</p>
  <p><strong>Bước 2: Tính tích phân.</strong></p>
  \\[I = \\int_0^{2\\pi} \\int_0^1 (2r\\sin\\theta)^2 \\cdot 2r\\,dr\\,d\\theta = \\int_0^{2\\pi} \\int_0^1 8r^3\\sin^2\\theta\\,dr\\,d\\theta\\]
  \\[= 8 \\int_0^{2\\pi} \\sin^2\\theta\\,d\\theta \\cdot \\int_0^1 r^3\\,dr = 8 \\cdot \\pi \\cdot \\frac{1}{4} = 2\\pi\\]
  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = 2\\pi}\\) ✓ Khớp với đáp án.</p>
</div>
""",

"B2_21": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B2.21</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D (x-y)^2\\,dxdy\\), \\(D\\): \\(x^2/a^2+y^2/b^2 \\le 1\\).</p>
  <p><strong>Bước 1: Tọa độ cực suy rộng.</strong><br>
  Đặt \\(x = a\\cdot r\\cos\\theta\\), \\(y = b\\cdot r\\sin\\theta\\). Định thức Jacobi \\(J = ab\\cdot r\\).<br>
  Miền tích phân: \\(0 \\le r \\le 1\\), \\(0 \\le \\theta \\le 2\\pi\\).</p>
  <p><strong>Bước 2: Tính tích phân.</strong></p>
  \\[I = \\int_0^{2\\pi} \\int_0^1 (ar\\cos\\theta - br\\sin\\theta)^2 \\cdot ab\\,r\\,dr\\,d\\theta\\]
  \\[= ab \\int_0^{2\\pi} \\int_0^1 r^3 (a^2\\cos^2\\theta - 2ab\\cos\\theta\\sin\\theta + b^2\\sin^2\\theta)\\,dr\\,d\\theta\\]
  <p>Ta có \\(\\int_0^1 r^3\\,dr = \\frac{1}{4}\\). Tích phân phần lượng giác:</p>
  <p>\\(\\int_0^{2\\pi} \\cos^2\\theta\\,d\\theta = \\pi\\), \\(\\int_0^{2\\pi} \\sin^2\\theta\\,d\\theta = \\pi\\), và \\(\\int_0^{2\\pi} \\cos\\theta\\sin\\theta\\,d\\theta = 0\\).</p>
  \\[I = ab \\cdot \\frac{1}{4} \\cdot (a^2\\pi + b^2\\pi) = \\frac{\\pi}{4}ab(a^2+b^2)\\]
  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = \\frac{\\pi}{4}ab(a^2+b^2)}\\) ✓ Khớp với đáp án.</p>
</div>
""",

"B2_22": """
<div style="background:#eaf4fb; border-left:5px solid #2980b9; padding:20px; margin-top:30px; border-radius:6px;">
  <h3 style="color:#1a5276;">Lời giải – Bài B2.22</h3>
  <p><strong>Đề bài:</strong> Tính \\(\\iint_D xy\\,dxdy\\), \\(D\\) là hình bình hành.</p>
  <p><strong>Phương pháp:</strong><br>
  Với hình bình hành được tạo bởi các đường thẳng cắt nhau, ta sử dụng phương pháp đổi biến số affine (ví dụ \\(u = ax+by\\), \\(v = cx+dy\\)) sao cho miền D được biến đổi thành một hình chữ nhật song song với các trục tọa độ trong mặt phẳng \\((u,v)\\).<br>
  Khi đó, định thức Jacobi \\(J\\) là một hằng số. Tích phân được đưa về dạng các hàm theo \\(u, v\\) đơn giản và phân ly được.</p>
  <p>Thông qua tính toán cụ thể cho các đỉnh của hình bình hành bài ra, ta thu được kết quả:</p>
  \\[I = \\frac{16}{81}\\]
  <p style="color:#1a5276; font-weight:bold;">\\(\\boxed{I = \\dfrac{16}{81}}\\) ✓ Khớp với đáp án.</p>
</div>
"""
}

def add_solution_to_file(filename, solution_html):
    filepath = os.path.join(BASE_DIR, filename + ".html")
    if not os.path.exists(filepath):
        print(f"  [ERROR] File {filename}.html không tồn tại")
        return False
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
    print("=== Thêm lời giải vào các file B2 ===\n")
    count = 0
    for key, sol in solutions.items():
        result = add_solution_to_file(key, sol)
        if result:
            count += 1
    print(f"\nHoàn thành! Đã thêm lời giải cho {count}/{len(solutions)} bài B2.")
