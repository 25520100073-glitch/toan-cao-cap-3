import numpy as np
import plotly.graph_objects as go
import os
from html_helper import create_html

def circle(x0, y0, r, t_start=0, t_end=2*np.pi):
    t = np.linspace(t_start, t_end, 100)
    return x0 + r*np.cos(t), y0 + r*np.sin(t)

# B2.1
fig = go.Figure()
x_out, y_out = circle(0, 0, 2, 0, np.pi/2)
x_in, y_in = circle(0, 0, 1, np.pi/2, 0)
fig.add_trace(go.Scatter(x=np.concatenate([x_out, x_in]), y=np.concatenate([y_out, y_in]), fill='toself', name='Miền D'))
create_html("B2_1.html", "Bài B2.1", r"\(\iint_D (x^2+y^2)^2 dxdy\), D: \(1 \le x^2+y^2 \le 4, x \ge 0, y \ge 0\)", r"\(21\pi/4\)", fig, "")

# B2.2
fig = go.Figure()
cx, cy = circle(0, 0, 1)
fig.add_trace(go.Scatter(x=cx, y=cy, fill='toself', name='Miền D'))
create_html("B2_2.html", "Bài B2.2", r"\(\iint_D (5x^2+2y^2) dxdy\), D: \(x^2+y^2 \le 1\)", r"\(7\pi/4\)", fig, "")

# B2.3
fig = go.Figure()
cx, cy = circle(0, 0, np.sqrt(2), -np.pi/2, np.pi/2)
fig.add_trace(go.Scatter(x=np.concatenate([cx, [0]]), y=np.concatenate([cy, [0]]), fill='toself', name='Miền D'))
create_html("B2_3.html", "Bài B2.3", r"\(\iint_D y^2 dxdy\), D: \(x^2+y^2 \le 2, x \ge 0\)", r"\(\pi/2\)", fig, "")

# B2.4
fig = go.Figure()
cx, cy = circle(2, 0, 2, np.pi, 2*np.pi)
fig.add_trace(go.Scatter(x=np.concatenate([cx, [0]]), y=np.concatenate([cy, [0]]), fill='toself', name='Miền D'))
create_html("B2_4.html", "Bài B2.4", r"\(\iint_D y dxdy\), D là nửa hình tròn \(x^2+y^2 \le 4x\) thoả \(y \le 0\)", r"\(-16/3\)", fig, "")

# B2.5
fig = go.Figure()
cx, cy = circle(0, 1, 1, -np.pi/2, np.pi/2)
fig.add_trace(go.Scatter(x=np.concatenate([cx, [0]]), y=np.concatenate([cy, [1]]), fill='toself', name='Miền D'))
create_html("B2_5.html", "Bài B2.5", r"\(\iint_D xydxdy\), D là nửa hình tròn tâm (0;1) bán kính 1, \(x \ge 0\)", r"\(2/3\)", fig, "")

# B2.6
fig = go.Figure()
t = np.linspace(-np.pi/4, 0, 100)
r = 2 * np.cos(t)
x_arc = r * np.cos(t)
y_arc = r * np.sin(t)
fig.add_trace(go.Scatter(x=np.concatenate([[0], x_arc]), y=np.concatenate([[0], y_arc]), fill='toself', name='Miền D'))
create_html("B2_6.html", "Bài B2.6", r"\(\iint_D xydxdy\), D giới hạn bởi \(y=-x\) và \(x^2+y^2=2x\) (diện tích nhỏ hơn)", r"\(-1/12\)", fig, "")

# B2.7
fig = go.Figure()
cx, cy = circle(0, 0, 1)
fig.add_trace(go.Scatter(x=cx, y=cy, fill='toself', name='Miền D'))
create_html("B2_7.html", "Bài B2.7", r"\(\iint_D (\sqrt{x^2+y^2}+1) dxdy\), D là hình tròn đơn vị", r"\(5\pi/3\)", fig, "")

# B2.8
fig = go.Figure()
cx, cy = circle(0, 0, 1, 0, np.pi)
fig.add_trace(go.Scatter(x=np.concatenate([cx, [0]]), y=np.concatenate([cy, [0]]), fill='toself', name='Miền D'))
create_html("B2_8.html", "Bài B2.8", r"\(\iint_D (x^2+y^2)e^{\sqrt{x^2+y^2}} dxdy\), D: \(x^2+y^2 \le 1, y \ge 0\)", r"\(2\pi(3-e)\)", fig, "")

# B2.9
fig = go.Figure()
x_out, y_out = circle(0, 0, 2)
x_in, y_in = circle(0, 0, 1, 2*np.pi, 0)
fig.add_trace(go.Scatter(x=np.concatenate([x_out, x_in]), y=np.concatenate([y_out, y_in]), fill='toself', name='Miền D'))
create_html("B2_9.html", "Bài B2.9", r"\(\iint_D \frac{\sqrt{x^2+y^2}-1}{x^2+y^2} dxdy\), D: \(1 \le x^2+y^2 \le 4\)", r"\(2\pi(1 - \ln 2)\)", fig, "")

# B2.10
fig = go.Figure()
x_out, y_out = circle(0, 0, 3, 0, np.pi/2)
x_in, y_in = circle(0, 0, 1, np.pi/2, 0)
fig.add_trace(go.Scatter(x=np.concatenate([x_out, x_in]), y=np.concatenate([y_out, y_in]), fill='toself', name='Miền D'))
create_html("B2_10.html", "Bài B2.10", r"\(\iint_D (x^2+y^2+1)^2 dxdy\), D giữa \(x^2+y^2=1\) và \(x^2+y^2=9\), \(x, y \ge 0\)", r"\(248\pi/3\)", fig, "")

# B2.11
fig = go.Figure()
cx, cy = circle(1, 0, 1, 0, np.pi)
fig.add_trace(go.Scatter(x=np.concatenate([cx, [0]]), y=np.concatenate([cy, [0]]), fill='toself', name='Miền D'))
create_html("B2_11.html", "Bài B2.11", r"\(\iint_D xydxdy\), D: \(x^2+y^2 \le 2x, y \ge 0\)", r"\(2/3\)", fig, "")

# B2.12
fig = go.Figure()
cx, cy = circle(0, 1, 1)
fig.add_trace(go.Scatter(x=cx, y=cy, fill='toself', name='Miền D'))
create_html("B2_12.html", "Bài B2.12", r"\(\iint_D \sqrt{(x^2+y^2)^3} dxdy\), D: \(x^2+y^2 \le 2y\)", r"\(512/75\)", fig, "")

# B2.13
fig = go.Figure()
cx, cy = circle(3, 0, 3, 0, np.pi)
fig.add_trace(go.Scatter(x=np.concatenate([cx, [0]]), y=np.concatenate([cy, [0]]), fill='toself', name='Miền D'))
create_html("B2_13.html", "Bài B2.13", r"\(\iint_D (x+y) dxdy\), D tâm (3;0) bk 3 lấy \(y \ge 0\)", r"\(27\pi/2 + 18\)", fig, "")

# B2.14
fig = go.Figure()
cx, cy = circle(0, 2, 2, -np.pi/2, np.pi/2)
fig.add_trace(go.Scatter(x=np.concatenate([cx, [0]]), y=np.concatenate([cy, [2]]), fill='toself', name='Miền D'))
create_html("B2_14.html", "Bài B2.14", r"\(\iint_D xy(x^2+y^2) dxdy\), D tâm (0;2) bk 2 lấy \(x \ge 0\)", r"\(256/3\)", fig, "")

# B2.15
fig = go.Figure()
x_out, y_out = circle(0, 0, 2)
x_in, y_in = circle(1, 0, 1, 2*np.pi, 0)
fig.add_trace(go.Scatter(x=np.concatenate([x_out, x_in]), y=np.concatenate([y_out, y_in]), fill='toself', name='Miền D'))
create_html("B2_15.html", "Bài B2.15", r"\(\iint_D y^2 dxdy\), D nằm giữa \(x^2+y^2=2x\) và \(x^2+y^2=4\)", r"\(15\pi/4\)", fig, "")

# B2.16 (Same as B2.6)
fig = go.Figure()
fig.add_trace(go.Scatter(x=np.concatenate([[0], x_arc]), y=np.concatenate([[0], y_arc]), fill='toself', name='Miền D'))
create_html("B2_16.html", "Bài B2.16", r"\(\iint_D xydxdy\), D giới hạn bởi \(y=-x\) và \(x^2+y^2=2x\)", r"\(-1/12\)", fig, "")

# B2.17
fig = go.Figure()
x_out, y_out = circle(0, 0, np.e**2 - 2)
x_in, y_in = circle(0, 0, np.e - 2, 2*np.pi, 0)
fig.add_trace(go.Scatter(x=np.concatenate([x_out, x_in]), y=np.concatenate([y_out, y_in]), fill='toself', name='Miền D'))
create_html("B2_17.html", "Bài B2.17", r"\(\iint_D \frac{\ln(\sqrt{x^2+y^2}+2)}{\dots} dxdy\)", r"\(3\pi\)", fig, "")

# B2.18
fig = go.Figure()
# Center (a,0) radius a, inside y=x and Oy
# Circle equation: r = 2a cos(t). Line y=x is t=pi/4.
t = np.linspace(np.pi/4, np.pi/2, 100)
x_arc = 2 * np.cos(t) * np.cos(t)
y_arc = 2 * np.cos(t) * np.sin(t)
fig.add_trace(go.Scatter(x=np.concatenate([[0], x_arc]), y=np.concatenate([[0], y_arc]), fill='toself', name='Miền D'))
create_html("B2_18.html", "Bài B2.18", r"\(\iint_D \sqrt{(4a^2-x^2-y^2)^3} dxdy\)", r"\(\frac{4a^5}{75}(30\pi - 43\sqrt{2})\)", fig, "")

# B2.19
fig = go.Figure()
# 2cos(t) <= r <= 4cos(t) and -pi/4 <= t <= pi/3
t = np.linspace(-np.pi/4, np.pi/3, 100)
x_out = 4 * np.cos(t) * np.cos(t)
y_out = 4 * np.cos(t) * np.sin(t)
x_in = 2 * np.cos(t[::-1]) * np.cos(t[::-1])
y_in = 2 * np.cos(t[::-1]) * np.sin(t[::-1])
fig.add_trace(go.Scatter(x=np.concatenate([x_out, x_in]), y=np.concatenate([y_out, y_in]), fill='toself', name='Miền D'))
create_html("B2_19.html", "Bài B2.19", r"\(\iint_D x^2y dxdy\), D: \(2x \le x^2+y^2 \le 4x\)", r"\(93/64\)", fig, "")

# B2.20
fig = go.Figure()
t = np.linspace(0, 2*np.pi, 100)
fig.add_trace(go.Scatter(x=1*np.cos(t), y=2*np.sin(t), fill='toself', name='Miền D'))
create_html("B2_20.html", "Bài B2.20", r"\(\iint_D y^2 dxdy\), D: \(4x^2+y^2=4\)", r"\(2\pi\)", fig, "")

# B2.21
fig = go.Figure()
fig.add_trace(go.Scatter(x=3*np.cos(t), y=2*np.sin(t), fill='toself', name='Miền D (ví dụ a=3, b=2)'))
create_html("B2_21.html", "Bài B2.21", r"\(\iint_D (x-y)^2 dxdy\), D: \(x^2/a^2+y^2/b^2 \le 1\)", r"\(\frac{\pi}{4}ab(a^2+b^2)\)", fig, "")

# B2.22
fig = go.Figure()
# x-y=0, x-y=1 => y=x, y=x-1
# 2x+y=1, 2x+y=3 => y=1-2x, y=3-2x
# Vertices: 
# x=1-2x => 3x=1 => (1/3, 1/3)
# x=3-2x => 3x=3 => (1, 1)
# x-1=1-2x => 3x=2 => (2/3, -1/3)
# x-1=3-2x => 3x=4 => (4/3, 1/3)
pts = [(1/3, 1/3), (1, 1), (4/3, 1/3), (2/3, -1/3), (1/3, 1/3)]
px, py = zip(*pts)
fig.add_trace(go.Scatter(x=px, y=py, fill='toself', name='Miền D'))
create_html("B2_22.html", "Bài B2.22", r"\(\iint_D xydxdy\), D là hình bình hành", r"\(16/81\)", fig, "")
