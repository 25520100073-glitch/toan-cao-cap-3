import numpy as np
import plotly.graph_objects as go
from html_helper import create_3d_projection_html

def solid_color(color):
    return [[0, color], [1, color]]

# B3.11
# z=2+x^2+y^2, x^2+y^2=1, Oxy(z=0)
theta = np.linspace(0, 2*np.pi, 50)
r = np.linspace(0, 1, 20)
R, Theta = np.meshgrid(r, theta)
X = R*np.cos(Theta)
Y = R*np.sin(Theta)
Z_top = 2 + R**2
Z_bot = np.zeros_like(R)
surfaces_3_11 = [
    go.Surface(x=X, y=Y, z=Z_top, colorscale=solid_color('lightblue'), opacity=0.8),
    go.Surface(x=X, y=Y, z=Z_bot, colorscale=solid_color('lightgreen'), opacity=0.8)
]
z_cyl = np.linspace(0, 1, 20)
Theta2, Z2 = np.meshgrid(theta, z_cyl)
# wall from z=0 up to z=2+1^2 = 3
# wait, Z2 goes from 0 to 1, we want it to go from 0 to 3
Z2_scaled = Z2 * 3.0
surfaces_3_11.append(go.Surface(x=np.cos(Theta2), y=np.sin(Theta2), z=Z2_scaled, colorscale=solid_color('orange'), opacity=0.8))
lines_3_11 = [
    go.Scatter3d(x=np.cos(theta), y=np.sin(theta), z=np.full_like(theta, 3), mode='lines', line=dict(color='red', width=4)),
    go.Scatter3d(x=np.cos(theta), y=np.sin(theta), z=np.zeros_like(theta), mode='lines', line=dict(color='blue', width=4))
]
domain_3_11 = [go.Scatter(x=np.cos(theta), y=np.sin(theta), fill='toself', fillcolor='rgba(255,165,0,0.4)', line=dict(color='orange'))]
create_3d_projection_html("B3_11.html", "Bài B3.11", r"Vật thể \(z=2+x^2+y^2, x^2+y^2=1, Oxy\)", "Hoàn thành vẽ", surfaces_3_11, lines_3_11, domain_3_11, "")

# B3.12
# Cone z=sqrt(x^2+y^2), z=1, z=2
r = np.linspace(0, 2, 30)
R, Theta = np.meshgrid(r, theta)
X = R*np.cos(Theta)
Y = R*np.sin(Theta)
Z_cone = R
# mask to keep only z between 1 and 2
Z_cone_surf = np.where((R >= 1) & (R <= 2), R, np.nan)
surfaces_3_12 = [go.Surface(x=X, y=Y, z=Z_cone_surf, colorscale=solid_color('lightblue'), opacity=0.8)]
r_top = np.linspace(0, 2, 20)
R_top, Theta_top = np.meshgrid(r_top, theta)
surfaces_3_12.append(go.Surface(x=R_top*np.cos(Theta_top), y=R_top*np.sin(Theta_top), z=np.full_like(R_top, 2.0), colorscale=solid_color('orange'), opacity=0.8))
r_bot = np.linspace(0, 1, 20)
R_bot, Theta_bot = np.meshgrid(r_bot, theta)
surfaces_3_12.append(go.Surface(x=R_bot*np.cos(Theta_bot), y=R_bot*np.sin(Theta_bot), z=np.full_like(R_bot, 1.0), colorscale=solid_color('lightgreen'), opacity=0.8))

lines_3_12 = [
    go.Scatter3d(x=2*np.cos(theta), y=2*np.sin(theta), z=np.full_like(theta, 2), mode='lines', line=dict(color='red', width=4)),
    go.Scatter3d(x=1*np.cos(theta), y=1*np.sin(theta), z=np.full_like(theta, 1), mode='lines', line=dict(color='blue', width=4))
]
domain_3_12 = [
    go.Scatter(x=2*np.cos(theta), y=2*np.sin(theta), fill='toself', fillcolor='rgba(100,100,255,0.4)', line=dict(color='blue')),
    go.Scatter(x=1*np.cos(theta), y=1*np.sin(theta), fill='toself', fillcolor='rgba(255,255,255,1.0)', line=dict(color='white'))
]
create_3d_projection_html("B3_12.html", "Bài B3.12", r"Vật thể \(z=\sqrt{x^2+y^2}, z=1, z=2\)", "Hoàn thành vẽ", surfaces_3_12, lines_3_12, domain_3_12, "")


# B3.13
# Cone z=sqrt(x^2+y^2), sphere x^2+y^2+z^2=4, above Oxy
r = np.linspace(0, np.sqrt(2), 30) # Intersection is r = sqrt(2), z = sqrt(2)
R, Theta = np.meshgrid(r, theta)
X = R*np.cos(Theta)
Y = R*np.sin(Theta)
Z_cone = R
Z_sphere = np.sqrt(4 - R**2)
surfaces_3_13 = [
    go.Surface(x=X, y=Y, z=Z_sphere, colorscale=solid_color('lightblue'), opacity=0.8),
    go.Surface(x=X, y=Y, z=Z_cone, colorscale=solid_color('orange'), opacity=0.8)
]
lines_3_13 = [
    go.Scatter3d(x=np.sqrt(2)*np.cos(theta), y=np.sqrt(2)*np.sin(theta), z=np.full_like(theta, np.sqrt(2)), mode='lines', line=dict(color='red', width=4))
]
domain_3_13 = [go.Scatter(x=np.sqrt(2)*np.cos(theta), y=np.sqrt(2)*np.sin(theta), fill='toself', fillcolor='rgba(0,255,255,0.4)', line=dict(color='cyan'))]
create_3d_projection_html("B3_13.html", "Bài B3.13", r"Vật thể \(z=\sqrt{x^2+y^2}, x^2+y^2+z^2=4\)", "Hoàn thành vẽ", surfaces_3_13, lines_3_13, domain_3_13, "")

# B3.14
# z=4-x^2-y^2, cylinder x^2+y^2=1, Oxy
r = np.linspace(0, 1, 20)
R, Theta = np.meshgrid(r, theta)
X = R*np.cos(Theta)
Y = R*np.sin(Theta)
Z_top = 4 - R**2
surfaces_3_14 = [
    go.Surface(x=X, y=Y, z=Z_top, colorscale=solid_color('lightblue'), opacity=0.8),
    go.Surface(x=X, y=Y, z=np.zeros_like(R), colorscale=solid_color('lightgreen'), opacity=0.8)
]
z_cyl = np.linspace(0, 1, 20)
Theta2, Z2 = np.meshgrid(theta, z_cyl)
surfaces_3_14.append(go.Surface(x=np.cos(Theta2), y=np.sin(Theta2), z=Z2*3, colorscale=solid_color('orange'), opacity=0.8))
lines_3_14 = [
    go.Scatter3d(x=np.cos(theta), y=np.sin(theta), z=np.full_like(theta, 3), mode='lines', line=dict(color='red', width=4)),
    go.Scatter3d(x=np.cos(theta), y=np.sin(theta), z=np.zeros_like(theta), mode='lines', line=dict(color='blue', width=4))
]
domain_3_14 = [go.Scatter(x=np.cos(theta), y=np.sin(theta), fill='toself', fillcolor='rgba(255,0,0,0.4)', line=dict(color='red'))]
create_3d_projection_html("B3_14.html", "Bài B3.14", r"Vật thể \(z=4-x^2-y^2, x^2+y^2=1, Oxy\)", "Hoàn thành vẽ", surfaces_3_14, lines_3_14, domain_3_14, "")

# B3.15
# z=sqrt(x^2+y^2), spheres r=1, r=2, z>=0
# Intersection of cone with sphere R is at radius r_cyl = R / sqrt(2)
r_cyl = np.linspace(1/np.sqrt(2), 2/np.sqrt(2), 30)
R, Theta = np.meshgrid(r_cyl, theta)
X = R*np.cos(Theta)
Y = R*np.sin(Theta)
Z_cone = R
surfaces_3_15 = [go.Surface(x=X, y=Y, z=Z_cone, colorscale=solid_color('orange'), opacity=0.8)]
# Top spherical cap (R=2) for r from 0 to 2/sqrt(2) = sqrt(2)
r_top = np.linspace(0, np.sqrt(2), 30)
R_top, Theta_top = np.meshgrid(r_top, theta)
Z_top = np.sqrt(4 - R_top**2)
surfaces_3_15.append(go.Surface(x=R_top*np.cos(Theta_top), y=R_top*np.sin(Theta_top), z=Z_top, colorscale=solid_color('lightblue'), opacity=0.8))
# Bottom spherical cap (R=1) for r from 0 to 1/sqrt(2)
r_bot = np.linspace(0, 1/np.sqrt(2), 30)
R_bot, Theta_bot = np.meshgrid(r_bot, theta)
Z_bot = np.sqrt(1 - R_bot**2)
surfaces_3_15.append(go.Surface(x=R_bot*np.cos(Theta_bot), y=R_bot*np.sin(Theta_bot), z=Z_bot, colorscale=solid_color('lightgreen'), opacity=0.8))

lines_3_15 = [
    go.Scatter3d(x=np.sqrt(2)*np.cos(theta), y=np.sqrt(2)*np.sin(theta), z=np.full_like(theta, np.sqrt(2)), mode='lines', line=dict(color='red', width=4)),
    go.Scatter3d(x=(1/np.sqrt(2))*np.cos(theta), y=(1/np.sqrt(2))*np.sin(theta), z=np.full_like(theta, 1/np.sqrt(2)), mode='lines', line=dict(color='blue', width=4))
]
domain_3_15 = [
    go.Scatter(x=np.sqrt(2)*np.cos(theta), y=np.sqrt(2)*np.sin(theta), fill='toself', fillcolor='rgba(0,100,255,0.4)', line=dict(color='cyan')),
    go.Scatter(x=(1/np.sqrt(2))*np.cos(theta), y=(1/np.sqrt(2))*np.sin(theta), fill='toself', fillcolor='rgba(255,255,255,1.0)', line=dict(color='white'))
]
create_3d_projection_html("B3_15.html", "Bài B3.15", r"Vật thể \(z=\sqrt{x^2+y^2}, x^2+y^2+z^2=1, x^2+y^2+z^2=4, z \ge 0\)", "Hoàn thành vẽ", surfaces_3_15, lines_3_15, domain_3_15, "")
