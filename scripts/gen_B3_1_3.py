import numpy as np
import plotly.graph_objects as go
from html_helper import create_3d_projection_html

def solid_color(color):
    return [[0, color], [1, color]]

# B3.1
# Box 0<=x<=1, 1<=y<=2, 0<=z<=2
# We can use Mesh3d for a simple box
x_box = [0,1,1,0, 0,1,1,0]
y_box = [1,1,2,2, 1,1,2,2]
z_box = [0,0,0,0, 2,2,2,2]
i_box = [0,0,0,0, 4,4,4,4, 0,1,2,3]
j_box = [1,2,3,1, 5,6,7,5, 4,5,6,7]
k_box = [2,3,0,2, 6,7,4,6, 1,2,3,0] # simplified, alphahull is easier
surfaces_3_1 = [go.Mesh3d(x=x_box, y=y_box, z=z_box, alphahull=0, opacity=0.4, color='cyan')]
# Edges for B3.1
lines_3_1 = []
for p1, p2 in [(0,1),(1,2),(2,3),(3,0), (4,5),(5,6),(6,7),(7,4), (0,4),(1,5),(2,6),(3,7)]:
    lines_3_1.append(go.Scatter3d(x=[x_box[p1], x_box[p2]], y=[y_box[p1], y_box[p2]], z=[z_box[p1], z_box[p2]], mode='lines', line=dict(color='blue', width=4)))
# Projection D
domain_3_1 = [go.Scatter(x=[0,1,1,0,0], y=[1,1,2,2,1], fill='toself', fillcolor='rgba(0,255,255,0.4)', line=dict(color='blue'))]

create_3d_projection_html("B3_1.html", "Bài B3.1", r"\(\iiint_\Omega x^3yz^2 dxdydz\), \(\Omega\) là hình hộp chữ nhật \(0 \le x \le 1, 1 \le y \le 2, 0 \le z \le 2\)", "1", surfaces_3_1, lines_3_1, domain_3_1, "")

# B3.2
# 0<=x<=1, sqrt(x)<=y<=1, 0<=z<=1-y
# Base is bounded by x=0, y=1, y=sqrt(x) (which is x=y^2). So y from 0 to 1, x from 0 to y^2.
# Wait, sqrt(x) <= y <= 1 for x in [0,1].
# This means y goes from 0 to 1, x goes from 0 to y^2.
y_grid = np.linspace(0, 1, 30)
x_grid = np.linspace(0, 1, 30)
Y, X = np.meshgrid(y_grid, x_grid)
# Top surface z = 1-y. But restricted to x <= y^2.
mask = X <= Y**2
Z_top = 1 - Y
Z_top[~mask] = np.nan
surfaces_3_2 = [
    go.Surface(x=X, y=Y, z=Z_top, colorscale=solid_color('lightblue'), opacity=0.8),
    go.Surface(x=X, y=Y, z=np.where(mask, 0, np.nan), colorscale=solid_color('lightgreen'), opacity=0.8)
]
# Draw vertical wall at y=sqrt(x) => x=y^2.
# t from 0 to 1. y=t, x=t^2, z from 0 to 1-t
t = np.linspace(0, 1, 30)
surfaces_3_2.append(go.Surface(
    x=np.array([t**2, t**2]),
    y=np.array([t, t]),
    z=np.array([np.zeros_like(t), 1-t]),
    colorscale=solid_color('orange'), opacity=0.8
))
# Vertical wall at y=1 is just a line because 1-y = 0.
# Edges
lines_3_2 = [
    go.Scatter3d(x=t**2, y=t, z=1-t, mode='lines', line=dict(color='red', width=4)), # top curve
    go.Scatter3d(x=t**2, y=t, z=np.zeros_like(t), mode='lines', line=dict(color='blue', width=4)), # bottom curve
    go.Scatter3d(x=[0,0], y=[0,1], z=[0,0], mode='lines', line=dict(color='green', width=4)), # x=0 on base
    go.Scatter3d(x=[0,0], y=[0,0], z=[0,1], mode='lines', line=dict(color='black', width=4)), # z-axis edge
    go.Scatter3d(x=[0,0], y=t, z=1-t, mode='lines', line=dict(color='black', width=4)), # top edge on x=0
]
# Projection D
domain_3_2 = [
    go.Scatter(x=np.concatenate([[0], t**2, [0]]), y=np.concatenate([[0], t, [1]]), fill='toself', fillcolor='rgba(255,165,0,0.4)', line=dict(color='orange'))
]
create_3d_projection_html("B3_2.html", "Bài B3.2", r"\(\iiint_\Omega xz dxdydz\), \(\Omega\): \(0 \le x \le 1, \sqrt{x} \le y \le 1, 0 \le z \le 1-y\)", "1/420", surfaces_3_2, lines_3_2, domain_3_2, "")

# B3.3
# Tetrahedron x+2y+z=6, x=0, y=0, z=0
x_tet = [0, 6, 0, 0]
y_tet = [0, 0, 3, 0]
z_tet = [0, 0, 0, 6]
surfaces_3_3 = [go.Mesh3d(x=x_tet, y=y_tet, z=z_tet, alphahull=0, opacity=0.5, color='magenta')]
lines_3_3 = []
for p1, p2 in [(0,1),(1,2),(2,0), (0,3),(1,3),(2,3)]:
    lines_3_3.append(go.Scatter3d(x=[x_tet[p1], x_tet[p2]], y=[y_tet[p1], y_tet[p2]], z=[z_tet[p1], z_tet[p2]], mode='lines', line=dict(color='purple', width=4)))
domain_3_3 = [go.Scatter(x=[0,6,0,0], y=[0,0,3,0], fill='toself', fillcolor='rgba(255,0,255,0.4)', line=dict(color='purple'))]
create_3d_projection_html("B3_3.html", "Bài B3.3", r"\(\iiint_\Omega z dxdydz\), \(\Omega\) là tứ diện \(x+2y+z=6, x=0, y=0, z=0\)", "27", surfaces_3_3, lines_3_3, domain_3_3, "")

