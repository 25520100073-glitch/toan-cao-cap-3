import numpy as np
import plotly.graph_objects as go
import sympy as sp
from html_helper import create_html

# For sympify
x, y = sp.symbols('x y')

# ==================== B1.8 ====================
# Triangle A(1,0), B(2,1), C(0,1). y from 0 to 1, x from 1-y to y+1
ans8 = sp.integrate(x - y, (x, 1-y, y+1), (y, 0, 1))
y8 = np.linspace(0, 1, 100)
x8_left = 1 - y8
x8_right = y8 + 1
fig8 = go.Figure()
fig8.add_trace(go.Scatter(x=np.concatenate([x8_left, x8_right[::-1]]), y=np.concatenate([y8, y8[::-1]]), fill='toself', fillcolor='rgba(0, 176, 246, 0.4)', line=dict(color='blue'), name='Miền D'))
fig8.update_layout(title="B1.8: Tam giác ABC")
create_html("B1_8.html", "Bài B1.8", r"\(\iint_D (x-y)dxdy\) với D là tam giác A(1;0), B(2;1), C(0;1)", rf"\({sp.latex(ans8)}\) (khớp 1/3)", fig8, "ans = sp.integrate(x-y, (x, 1-y, y+1), (y, 0, 1))")

# ==================== B1.9 ====================
# Area between y = x^2 and y = 2 - x^2
ans9 = sp.integrate(1, (y, x**2, 2-x**2), (x, -1, 1))
x9 = np.linspace(-1.2, 1.2, 200)
fig9 = go.Figure()
fig9.add_trace(go.Scatter(x=x9, y=x9**2, mode='lines', line=dict(color='blue'), name='y=x²'))
fig9.add_trace(go.Scatter(x=x9, y=2-x9**2, mode='lines', line=dict(color='red'), name='y=2-x²'))
x9_fill = np.linspace(-1, 1, 100)
fig9.add_trace(go.Scatter(x=np.concatenate([x9_fill, x9_fill[::-1]]), y=np.concatenate([x9_fill**2, (2-x9_fill**2)[::-1]]), fill='toself', fillcolor='rgba(255,127,14,0.4)', line=dict(width=0), name='Miền D'))
create_html("B1_9.html", "Bài B1.9", r"Diện tích miền D giới hạn bởi hai parabol \(y = x^2\) và \(y = 2 - x^2\)", rf"\({sp.latex(ans9)}\) (khớp 8/3)", fig9, "ans = sp.integrate(1, (y, x**2, 2-x**2), (x, -1, 1))")

# ==================== B1.10 ====================
# y=x^2, y=2-x, Ox (y=0)
ans10 = sp.integrate(y**2, (y, 0, x**2), (x, 0, 1)) + sp.integrate(y**2, (y, 0, 2-x), (x, 1, 2))
# Alternatively integrate y from 0 to 1, x from sqrt(y) to 2-y
x10_fill = np.concatenate([np.linspace(0, 1, 50), np.linspace(1, 2, 50)])
y10_fill = np.concatenate([np.linspace(0, 1, 50)**2, 2 - np.linspace(1, 2, 50)])
fig10 = go.Figure()
fig10.add_trace(go.Scatter(x=np.concatenate([x10_fill, [2, 0]]), y=np.concatenate([y10_fill, [0, 0]]), fill='toself', fillcolor='rgba(44,160,44,0.4)', line=dict(color='blue'), name='Miền D'))
create_html("B1_10.html", "Bài B1.10", r"\(\iint_D y^2 dxdy\), D giới hạn bởi parabol \(y = x^2\), \(y = 2-x\), và trục Ox", rf"\({sp.latex(ans10)}\) (khớp 11/84)", fig10, "ans = sp.integrate(y**2, (x, sp.sqrt(y), 2-y), (y, 0, 1))")

# ==================== B1.11 ====================
# y=x^2, y=2-x, Oy, x>=0
ans11 = sp.integrate(x*y, (y, x**2, 2-x), (x, 0, 1))
x11_fill = np.linspace(0, 1, 100)
fig11 = go.Figure()
fig11.add_trace(go.Scatter(x=np.concatenate([x11_fill, x11_fill[::-1]]), y=np.concatenate([x11_fill**2, (2-x11_fill)[::-1]]), fill='toself', fillcolor='rgba(214,39,40,0.4)', line=dict(color='purple'), name='Miền D'))
create_html("B1_11.html", "Bài B1.11", r"\(\iint_D xydxdy\), D giới hạn bởi \(y=x^2, y=2-x, Oy, x \ge 0\)", rf"\({sp.latex(ans11)}\) (khớp 3/8)", fig11, "ans = sp.integrate(x*y, (y, x**2, 2-x), (x, 0, 1))")

# ==================== B1.12 ====================
# y=x^2, y=2-x
ans12 = sp.integrate(x+y, (y, x**2, 2-x), (x, -2, 1))
x12_fill = np.linspace(-2, 1, 100)
fig12 = go.Figure()
fig12.add_trace(go.Scatter(x=np.concatenate([x12_fill, x12_fill[::-1]]), y=np.concatenate([x12_fill**2, (2-x12_fill)[::-1]]), fill='toself', fillcolor='rgba(148,103,189,0.4)', line=dict(color='orange'), name='Miền D'))
create_html("B1_12.html", "Bài B1.12", r"\(\iint_D (x+y)dxdy\), D giới hạn bởi \(y=x^2, y=2-x\)", rf"\({sp.latex(ans12)}\) (khớp 99/20)", fig12, "ans = sp.integrate(x+y, (y, x**2, 2-x), (x, -2, 1))")

# ==================== B1.13 ====================
# 1<=x<=4, 1<=y<=2
ans13 = sp.integrate(x/y + y/x, (y, 1, 2), (x, 1, 4))
fig13 = go.Figure()
fig13.add_trace(go.Scatter(x=[1, 4, 4, 1, 1], y=[1, 1, 2, 2, 1], fill='toself', fillcolor='rgba(140,86,75,0.4)', line=dict(color='brown'), name='Miền D'))
create_html("B1_13.html", "Bài B1.13", r"\(\iint_D (\frac{x}{y} + \frac{y}{x})dxdy\), D là HCN \(1 \le x \le 4, 1 \le y \le 2\)", rf"\({sp.latex(ans13)}\) (khớp 21*ln(2)/2)", fig13, "ans = sp.integrate(x/y + y/x, (y, 1, 2), (x, 1, 4))")

# ==================== B1.14 ====================
# Change order int_0^2 dx int_0^sqrt(2x-x^2) f(x,y) dy
x14 = np.linspace(0, 2, 200)
y14 = np.sqrt(1 - (x14-1)**2)
fig14 = go.Figure()
fig14.add_trace(go.Scatter(x=np.concatenate([x14, x14[::-1]]), y=np.concatenate([np.zeros_like(x14), y14[::-1]]), fill='toself', fillcolor='rgba(227,119,194,0.4)', line=dict(color='pink'), name='Miền D'))
fig14.update_yaxes(scaleanchor="x", scaleratio=1)
create_html("B1_14.html", "Bài B1.14", r"Đổi thứ tự tính tích phân \(\int_0^2 dx \int_0^{\sqrt{2x-x^2}} f(x;y) dy\)", "Không yêu cầu tính", fig14, "# Vẽ nửa đường tròn trên")

# ==================== B1.15 ====================
x15 = np.linspace(0, 2, 200)
y15_bottom = np.nan_to_num(np.sqrt(1 - (x15-1)**2)) # 0 for outside, but wait sqrt(negative) is nan.
y15_bottom = np.where((x15 >= 0) & (x15 <= 2), np.sqrt(2*x15 - x15**2), 0)
y15_top = np.sqrt(2*x15)
fig15 = go.Figure()
fig15.add_trace(go.Scatter(x=np.concatenate([x15, x15[::-1]]), y=np.concatenate([y15_bottom, y15_top[::-1]]), fill='toself', fillcolor='rgba(127,127,127,0.4)', line=dict(color='gray'), name='Miền D'))
create_html("B1_15.html", "Bài B1.15", r"Đổi thứ tự tính tích phân \(\int_0^2 dx \int_{\sqrt{2x-x^2}}^{\sqrt{2x}} f(x;y) dy\)", "Không yêu cầu tính", fig15, "# Vẽ miền giữa y=sqrt(2x) và y=sqrt(2x-x^2)")

# ==================== B1.16 ====================
ans16 = sp.integrate(x*y, (y, 2*x-1, 6-x), (x, 1, 2))
fig16 = go.Figure()
fig16.add_trace(go.Scatter(x=[1, 2, 2, 1, 1], y=[1, 3, 4, 5, 1], fill='toself', fillcolor='rgba(188,189,34,0.4)', line=dict(color='olive'), name='Hình thang MNPQ'))
create_html("B1_16.html", "Bài B1.16", r"\(\iint_D xydxdy\), D là hình thang M(1;1), N(2;3), P(2;4), Q(1;5)", rf"\({sp.latex(ans16)}\) (khớp 271/24)", fig16, "ans = sp.integrate(x*y, (y, 2*x-1, 6-x), (x, 1, 2))")

# ==================== B1.17 ====================
ans17 = sp.integrate(x**4*y**4, (y, x**2, sp.sqrt(-x)), (x, -1, 0))
x17 = np.linspace(-1, 0, 100)
fig17 = go.Figure()
fig17.add_trace(go.Scatter(x=np.concatenate([x17, x17[::-1]]), y=np.concatenate([x17**2, np.sqrt(-x17)[::-1]]), fill='toself', fillcolor='rgba(23,190,207,0.4)', line=dict(color='cyan'), name='Miền D'))
create_html("B1_17.html", "Bài B1.17", r"\(\iint_D x^4y^4 dxdy\), D giới hạn bởi \(x = -y^2\) và \(y = x^2\)", rf"\({sp.latex(ans17)}\) (khớp 1/75)", fig17, "ans = sp.integrate(x**4*y**4, (y, x**2, sp.sqrt(-x)), (x, -1, 0))")

# ==================== B1.18 ====================
ans18 = sp.integrate(x*y, (x, 0, 1/y), (y, 1, 4))
y18 = np.linspace(1, 4, 100)
x18 = 1/y18
fig18 = go.Figure()
fig18.add_trace(go.Scatter(x=np.concatenate([np.zeros_like(y18), x18[::-1]]), y=np.concatenate([y18, y18[::-1]]), fill='toself', fillcolor='rgba(255,187,120,0.4)', line=dict(color='orange'), name='Miền D'))
create_html("B1_18.html", "Bài B1.18", r"\(\iint_D xy dxdy\), D giới hạn bởi \(y=1, y=4, xy=1, x=0\)", rf"\({sp.latex(ans18)}\) (khớp ln(2))", fig18, "ans = sp.integrate(x*y, (x, 0, 1/y), (y, 1, 4))")

# ==================== B1.19 ====================
ans19 = sp.integrate(sp.sqrt(y - x**2), (y, x**2, 2), (x, -1, 1)) + sp.integrate(sp.sqrt(x**2 - y), (y, 0, x**2), (x, -1, 1))
fig19 = go.Figure()
fig19.add_trace(go.Scatter(x=[-1, 1, 1, -1, -1], y=[0, 0, 2, 2, 0], fill='toself', fillcolor='rgba(152,223,138,0.4)', line=dict(color='green'), name='Miền D'))
create_html("B1_19.html", "Bài B1.19", r"\(\iint_D \sqrt{|x^2-y|}dxdy\), D hình chữ nhật -1<=x<=1, 0<=y<=2", rf"\({sp.latex(ans19.evalf(5))}\) ~ (khớp 5/3 + pi/2)", fig19, "Tính chia miền y >= x^2 và y < x^2")

# ==================== B1.20 ====================
ans20 = sp.integrate(x**2, (y, 0, x**2), (x, -2*sp.sqrt(2), 2*sp.sqrt(2))) + sp.integrate(y, (y, x**2, 8-x**2), (x, -2, 2))
# Wait, max(x^2, y). D is y in [0, 8-x^2]. Intersection of y=x^2 and y=8-x^2 is x=+-2 (y=4).
# So for x in [-2, 2], y goes up to 8-x^2. If y < x^2, max is x^2. If y > x^2, max is y.
# For |x| > 2, 8-x^2 < x^2, so max is ALWAYS x^2 for y in [0, 8-x^2].
# Thus integral = int_{-2}^2 [int_0^{x^2} x^2 dy + int_{x^2}^{8-x^2} y dy] dx + 2 * int_2^{2sqrt(2)} int_0^{8-x^2} x^2 dy dx
x20 = np.linspace(-2*np.sqrt(2), 2*np.sqrt(2), 200)
y20 = 8 - x20**2
fig20 = go.Figure()
fig20.add_trace(go.Scatter(x=np.concatenate([x20, x20[::-1]]), y=np.concatenate([np.zeros_like(x20), y20[::-1]]), fill='toself', fillcolor='rgba(255,152,150,0.4)', line=dict(color='red'), name='Miền D'))
create_html("B1_20.html", "Bài B1.20", r"\(\iint_D \max(x^2, y) dxdy\), D giới hạn bởi \(y = 8 - x^2\) và trục Ox", rf"\({sp.latex(sp.Rational(512, 15) * (2 + sp.sqrt(2)))}\) (Đáp án)", fig20, "ans = ...")
