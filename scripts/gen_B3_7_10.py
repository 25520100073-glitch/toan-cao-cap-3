import numpy as np
import plotly.graph_objects as go
from html_helper import create_3d_projection_html

def solid_color(color):
    return [[0, color], [1, color]]

# B3.7
# z=1+x^2+y^2, x=0, y=0, z=0, x+y=1
x_grid = np.linspace(0, 1, 30)
y_grid = np.linspace(0, 1, 30)
X, Y = np.meshgrid(x_grid, y_grid)
mask = X + Y <= 1
Z_top = 1 + X**2 + Y**2
Z_top[~mask] = np.nan
surfaces_3_7 = [
    go.Surface(x=X, y=Y, z=Z_top, colorscale=solid_color('lightblue'), opacity=0.8),
    go.Surface(x=X, y=Y, z=np.where(mask, 0, np.nan), colorscale=solid_color('lightgreen'), opacity=0.8)
]
# walls
t = np.linspace(0, 1, 30)
zw = np.linspace(0, 1, 10)
T, ZW = np.meshgrid(t, zw)
# x=0 wall
surfaces_3_7.append(go.Surface(x=np.zeros_like(T), y=T, z=ZW*(1+T**2), colorscale=solid_color('orange'), opacity=0.8))
# y=0 wall
surfaces_3_7.append(go.Surface(x=T, y=np.zeros_like(T), z=ZW*(1+T**2), colorscale=solid_color('orange'), opacity=0.8))
# x+y=1 wall => y=1-x
surfaces_3_7.append(go.Surface(x=T, y=1-T, z=ZW*(1+T**2+(1-T)**2), colorscale=solid_color('orange'), opacity=0.8))
# Edges
lines_3_7 = [
    go.Scatter3d(x=np.zeros_like(t), y=t, z=1+t**2, mode='lines', line=dict(color='red', width=4)),
    go.Scatter3d(x=t, y=np.zeros_like(t), z=1+t**2, mode='lines', line=dict(color='red', width=4)),
    go.Scatter3d(x=t, y=1-t, z=1+t**2+(1-t)**2, mode='lines', line=dict(color='red', width=4)),
    go.Scatter3d(x=[0,1,0,0], y=[0,0,1,0], z=[0,0,0,0], mode='lines', line=dict(color='blue', width=4)),
    go.Scatter3d(x=[0,0], y=[0,0], z=[0,1], mode='lines', line=dict(color='black', width=4)),
    go.Scatter3d(x=[1,1], y=[0,0], z=[0,2], mode='lines', line=dict(color='black', width=4)),
    go.Scatter3d(x=[0,0], y=[1,1], z=[0,2], mode='lines', line=dict(color='black', width=4)),
]
domain_3_7 = [go.Scatter(x=[0,1,0,0], y=[0,0,1,0], fill='toself', fillcolor='rgba(255,165,0,0.4)', line=dict(color='orange'))]
create_3d_projection_html("B3_7.html", "Bài B3.7", r"Thế tích vật thể giới hạn bởi \(z=1+x^2+y^2\) và \(x=0, y=0, z=0, x+y=1\)", "2/3", surfaces_3_7, lines_3_7, domain_3_7, "")


# B3.8
# y=x^2, y=4x^2, y=1, z=0, z=1
x_grid = np.linspace(-1, 1, 50)
y_grid = np.linspace(0, 1, 50)
X, Y = np.meshgrid(x_grid, y_grid)
mask = (Y >= X**2) & (Y <= 4*X**2) & (Y <= 1)
Z_top = np.full_like(X, 1.0)
Z_top[~mask] = np.nan
surfaces_3_8 = [
    go.Surface(x=X, y=Y, z=Z_top, colorscale=solid_color('lightblue'), opacity=0.8),
    go.Surface(x=X, y=Y, z=np.where(mask, 0.0, np.nan), colorscale=solid_color('lightgreen'), opacity=0.8)
]
t = np.linspace(0, 1, 30) # y from 0 to 1
T, ZW = np.meshgrid(t, zw)
# walls y=x^2 => x=+-sqrt(y)
surfaces_3_8.append(go.Surface(x=np.sqrt(T), y=T, z=ZW, colorscale=solid_color('orange'), opacity=0.8))
surfaces_3_8.append(go.Surface(x=-np.sqrt(T), y=T, z=ZW, colorscale=solid_color('orange'), opacity=0.8))
# walls y=4x^2 => x=+-sqrt(y)/2
surfaces_3_8.append(go.Surface(x=np.sqrt(T)/2, y=T, z=ZW, colorscale=solid_color('magenta'), opacity=0.8))
surfaces_3_8.append(go.Surface(x=-np.sqrt(T)/2, y=T, z=ZW, colorscale=solid_color('magenta'), opacity=0.8))
# y=1 wall
x_wall_y1 = np.linspace(0.5, 1, 10)
XW, ZW2 = np.meshgrid(x_wall_y1, zw)
surfaces_3_8.append(go.Surface(x=XW, y=np.ones_like(XW), z=ZW2, colorscale=solid_color('yellow'), opacity=0.8))
surfaces_3_8.append(go.Surface(x=-XW, y=np.ones_like(XW), z=ZW2, colorscale=solid_color('yellow'), opacity=0.8))
# Edges
lines_3_8 = []
for z_level in [0, 1]:
    lines_3_8.append(go.Scatter3d(x=np.sqrt(t), y=t, z=np.full_like(t, z_level), mode='lines', line=dict(color='red', width=4)))
    lines_3_8.append(go.Scatter3d(x=-np.sqrt(t), y=t, z=np.full_like(t, z_level), mode='lines', line=dict(color='red', width=4)))
    lines_3_8.append(go.Scatter3d(x=np.sqrt(t)/2, y=t, z=np.full_like(t, z_level), mode='lines', line=dict(color='blue', width=4)))
    lines_3_8.append(go.Scatter3d(x=-np.sqrt(t)/2, y=t, z=np.full_like(t, z_level), mode='lines', line=dict(color='blue', width=4)))
    lines_3_8.append(go.Scatter3d(x=[0.5, 1], y=[1, 1], z=[z_level, z_level], mode='lines', line=dict(color='green', width=4)))
    lines_3_8.append(go.Scatter3d(x=[-0.5, -1], y=[1, 1], z=[z_level, z_level], mode='lines', line=dict(color='green', width=4)))
for x_vert in [1, 0.5, -0.5, -1]:
    lines_3_8.append(go.Scatter3d(x=[x_vert, x_vert], y=[1, 1], z=[0, 1], mode='lines', line=dict(color='black', width=4)))
lines_3_8.append(go.Scatter3d(x=[0,0], y=[0,0], z=[0,1], mode='lines', line=dict(color='black', width=4)))

x_fill = np.linspace(0, 1, 50)
domain_3_8 = [
    go.Scatter(x=np.concatenate([np.sqrt(t), (np.sqrt(t)/2)[::-1]]), y=np.concatenate([t, t[::-1]]), fill='toself', fillcolor='rgba(255,0,0,0.4)', line=dict(width=0)),
    go.Scatter(x=np.concatenate([-np.sqrt(t), (-np.sqrt(t)/2)[::-1]]), y=np.concatenate([t, t[::-1]]), fill='toself', fillcolor='rgba(255,0,0,0.4)', line=dict(width=0)),
]
create_3d_projection_html("B3_8.html", "Bài B3.8", r"Thể tích vật thể \(y=x^2, y=4x^2, y=1, z=0, z=1\)", "2/3", surfaces_3_8, lines_3_8, domain_3_8, "")


# B3.9
# (x-a)^2+(y-b)^2=R^2, z=h, z=k. We pick a=0, b=0, R=1, h=0, k=2 for visualization.
theta = np.linspace(0, 2*np.pi, 50)
z_cyl = np.linspace(0, 2, 20)
Theta, Z = np.meshgrid(theta, z_cyl)
X = np.cos(Theta)
Y = np.sin(Theta)
surfaces_3_9 = [go.Surface(x=X, y=Y, z=Z, colorscale=solid_color('lightblue'), opacity=0.8)]
r = np.linspace(0, 1, 20)
R, Theta = np.meshgrid(r, theta)
surfaces_3_9.extend([
    go.Surface(x=R*np.cos(Theta), y=R*np.sin(Theta), z=np.full_like(R, 2.0), colorscale=solid_color('orange'), opacity=0.8),
    go.Surface(x=R*np.cos(Theta), y=R*np.sin(Theta), z=np.zeros_like(R), colorscale=solid_color('lightgreen'), opacity=0.8)
])
lines_3_9 = [
    go.Scatter3d(x=np.cos(theta), y=np.sin(theta), z=np.full_like(theta, 2), mode='lines', line=dict(color='red', width=4)),
    go.Scatter3d(x=np.cos(theta), y=np.sin(theta), z=np.zeros_like(theta), mode='lines', line=dict(color='blue', width=4))
]
domain_3_9 = [go.Scatter(x=np.cos(theta), y=np.sin(theta), fill='toself', fillcolor='rgba(0,255,0,0.4)', line=dict(color='green'))]
create_3d_projection_html("B3_9.html", "Bài B3.9", r"\(\iiint_\Omega z^2 dxdydz\), \(\Omega\) là khối trụ (ví dụ R=1, h=0, k=2)", r"\(\frac{\pi R^2}{3}(k^3-h^3)\)", surfaces_3_9, lines_3_9, domain_3_9, "")

# B3.10
# z=x^2+y^2 and z=2-x^2-y^2
theta = np.linspace(0, 2*np.pi, 50)
r = np.linspace(0, 1, 20)
R, Theta = np.meshgrid(r, theta)
X = R*np.cos(Theta)
Y = R*np.sin(Theta)
Z_bot = R**2
Z_top = 2 - R**2
surfaces_3_10 = [
    go.Surface(x=X, y=Y, z=Z_top, colorscale=solid_color('lightblue'), opacity=0.8),
    go.Surface(x=X, y=Y, z=Z_bot, colorscale=solid_color('orange'), opacity=0.8)
]
lines_3_10 = [go.Scatter3d(x=np.cos(theta), y=np.sin(theta), z=np.full_like(theta, 1), mode='lines', line=dict(color='red', width=4))]
domain_3_10 = [go.Scatter(x=np.cos(theta), y=np.sin(theta), fill='toself', fillcolor='rgba(255,0,255,0.4)', line=dict(color='purple'))]
create_3d_projection_html("B3_10.html", "Bài B3.10", r"Vẽ vật thể \(\Omega\) giới hạn bởi \(z=x^2+y^2, z=2-x^2-y^2\)", "Hoàn thành vẽ", surfaces_3_10, lines_3_10, domain_3_10, "")
