import numpy as np
import plotly.graph_objects as go
from html_helper import create_3d_projection_html

def solid_color(color):
    return [[0, color], [1, color]]

# B3.4
# x^2+z^2=1, y+z=2, y=0
theta = np.linspace(0, 2*np.pi, 50)
r = np.linspace(0, 1, 20)
R, Theta = np.meshgrid(r, theta)
# Cylinder wall
X_wall = np.cos(Theta[:, -1:]) * np.ones((50, 2))
Z_wall = np.sin(Theta[:, -1:]) * np.ones((50, 2))
Y_wall = np.zeros((50, 2))
Y_wall[:, 1] = 2 - Z_wall[:, 1]
# Top slanted cap
X_top = R * np.cos(Theta)
Z_top = R * np.sin(Theta)
Y_top = 2 - Z_top
# Bottom cap
Y_bot = np.zeros_like(Y_top)

surfaces_3_4 = [
    go.Surface(x=X_wall, y=Y_wall, z=Z_wall, colorscale=solid_color('lightblue'), opacity=0.8),
    go.Surface(x=X_top, y=Y_top, z=Z_top, colorscale=solid_color('orange'), opacity=0.8),
    go.Surface(x=X_top, y=Y_bot, z=Z_top, colorscale=solid_color('lightgreen'), opacity=0.8)
]
# Edges
lines_3_4 = [
    go.Scatter3d(x=np.cos(theta), y=2-np.sin(theta), z=np.sin(theta), mode='lines', line=dict(color='red', width=4)), # top edge
    go.Scatter3d(x=np.cos(theta), y=np.zeros_like(theta), z=np.sin(theta), mode='lines', line=dict(color='blue', width=4)), # bottom edge
]
# Projection D on Oxy
x_proj = np.linspace(-1, 1, 100)
y_proj_max = 2 + np.sqrt(1 - x_proj**2)
domain_3_4 = [
    go.Scatter(x=np.concatenate([x_proj, x_proj[::-1]]), y=np.concatenate([np.zeros_like(x_proj), y_proj_max[::-1]]), fill='toself', fillcolor='rgba(255,165,0,0.4)', line=dict(color='orange'))
]
create_3d_projection_html("B3_4.html", "Bài B3.4", r"\(\iiint_\Omega \dots\), \(\Omega\): \(x^2+z^2=1, y+z=2, y=0\)", "4pi/3", surfaces_3_4, lines_3_4, domain_3_4, "")

# B3.5
# |x|+|y|+|z|<=1
x_oct = [1, -1, 0, 0, 0, 0]
y_oct = [0, 0, 1, -1, 0, 0]
z_oct = [0, 0, 0, 0, 1, -1]
surfaces_3_5 = [go.Mesh3d(x=x_oct, y=y_oct, z=z_oct, alphahull=0, opacity=0.5, color='magenta')]
lines_3_5 = []
# Edges: connect (1,0,0) to all (0,+-1,0) and (0,0,+-1), etc
for i, j in [(0,2),(0,3),(0,4),(0,5), (1,2),(1,3),(1,4),(1,5), (2,4),(2,5),(3,4),(3,5)]:
    lines_3_5.append(go.Scatter3d(x=[x_oct[i], x_oct[j]], y=[y_oct[i], y_oct[j]], z=[z_oct[i], z_oct[j]], mode='lines', line=dict(color='purple', width=3)))
# Projection D on Oxy: |x|+|y|<=1 => square diamond
domain_3_5 = [go.Scatter(x=[1,0,-1,0,1], y=[0,1,0,-1,0], fill='toself', fillcolor='rgba(255,0,255,0.4)', line=dict(color='purple'))]
create_3d_projection_html("B3_5.html", "Bài B3.5", r"\(\iiint_\Omega (x^2+y^2+z^2) dxdydz\), \(\Omega\): \(|x|+|y|+|z| \le a\)", "2a^5/5", surfaces_3_5, lines_3_5, domain_3_5, "")

# B3.6
# z = 2-x^2-y^2, x in [-1,1], y in [-1,1], z=0
x_grid = np.linspace(-1, 1, 30)
y_grid = np.linspace(-1, 1, 30)
X, Y = np.meshgrid(x_grid, y_grid)
Z_top = 2 - X**2 - Y**2
surfaces_3_6 = [
    go.Surface(x=X, y=Y, z=Z_top, colorscale=solid_color('lightblue'), opacity=0.8),
    go.Surface(x=X, y=Y, z=np.zeros_like(X), colorscale=solid_color('lightgreen'), opacity=0.8)
]
# Add 4 vertical walls x=+-1, y=+-1 from z=0 to z=2-x^2-y^2
t = np.linspace(-1, 1, 30)
z_wall = np.linspace(0, 1, 10)
T, ZW = np.meshgrid(t, z_wall)
# wall x=1
surfaces_3_6.append(go.Surface(x=np.ones_like(T), y=T, z=ZW * (2 - 1 - T**2), colorscale=solid_color('orange'), opacity=0.8))
# wall x=-1
surfaces_3_6.append(go.Surface(x=-np.ones_like(T), y=T, z=ZW * (2 - 1 - T**2), colorscale=solid_color('orange'), opacity=0.8))
# wall y=1
surfaces_3_6.append(go.Surface(x=T, y=np.ones_like(T), z=ZW * (2 - T**2 - 1), colorscale=solid_color('orange'), opacity=0.8))
# wall y=-1
surfaces_3_6.append(go.Surface(x=T, y=-np.ones_like(T), z=ZW * (2 - T**2 - 1), colorscale=solid_color('orange'), opacity=0.8))

# Edges
lines_3_6 = [
    go.Scatter3d(x=t, y=np.ones_like(t), z=2-t**2-1, mode='lines', line=dict(color='red', width=4)),
    go.Scatter3d(x=t, y=-np.ones_like(t), z=2-t**2-1, mode='lines', line=dict(color='red', width=4)),
    go.Scatter3d(x=np.ones_like(t), y=t, z=2-1-t**2, mode='lines', line=dict(color='red', width=4)),
    go.Scatter3d(x=-np.ones_like(t), y=t, z=2-1-t**2, mode='lines', line=dict(color='red', width=4)),
    # Bottom square
    go.Scatter3d(x=[-1,1,1,-1,-1], y=[-1,-1,1,1,-1], z=[0,0,0,0,0], mode='lines', line=dict(color='blue', width=4))
]
domain_3_6 = [go.Scatter(x=[-1,1,1,-1,-1], y=[-1,-1,1,1,-1], fill='toself', fillcolor='rgba(0,0,255,0.4)', line=dict(color='blue'))]
create_3d_projection_html("B3_6.html", "Bài B3.6", r"\(\iiint_\Omega (x^2+z) dxdydz\), \(\Omega\) giới hạn bởi \(z=2-x^2-y^2\) và \(x=\pm 1, y=\pm 1, z=0\)", "32/3", surfaces_3_6, lines_3_6, domain_3_6, "")

