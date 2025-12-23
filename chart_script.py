"""
Скрипт для создания визуализации натальной карты с использованием Plotly.
Требует установки: pip install plotly numpy kaleido
"""

try:
    import plotly.graph_objects as go
    import numpy as np
except ImportError as e:
    print(f"Ошибка: Не установлены необходимые библиотеки: {e}")
    print("Установите их командой: pip install plotly numpy kaleido")
    exit(1)

# Create figure with black background
fig = go.Figure()

# Zodiac signs with their symbols and elements
zodiac_signs = [
    {"name": "Aries", "symbol": "♈", "element": "fire", "color": "#DB4545"},
    {"name": "Taurus", "symbol": "♉", "element": "earth", "color": "#2E8B57"},
    {"name": "Gemini", "symbol": "♊", "element": "air", "color": "#D2BA4C"},
    {"name": "Cancer", "symbol": "♋", "element": "water", "color": "#1FB8CD"},
    {"name": "Leo", "symbol": "♌", "element": "fire", "color": "#DB4545"},
    {"name": "Virgo", "symbol": "♍", "element": "earth", "color": "#2E8B57"},
    {"name": "Libra", "symbol": "♎", "element": "air", "color": "#D2BA4C"},
    {"name": "Scorpio", "symbol": "♏", "element": "water", "color": "#1FB8CD"},
    {"name": "Sagittarius", "symbol": "♐", "element": "fire", "color": "#DB4545"},
    {"name": "Capricorn", "symbol": "♑", "element": "earth", "color": "#2E8B57"},
    {"name": "Aquarius", "symbol": "♒", "element": "air", "color": "#D2BA4C"},
    {"name": "Pisces", "symbol": "♓", "element": "water", "color": "#1FB8CD"}
]

# Planets with symbols
planets = [
    {"name": "Sun", "symbol": "☉", "angle": 45},
    {"name": "Moon", "symbol": "☽", "angle": 120},
    {"name": "Mercury", "symbol": "☿", "angle": 60},
    {"name": "Venus", "symbol": "♀", "angle": 30},
    {"name": "Mars", "symbol": "♂", "angle": 200},
    {"name": "Jupiter", "symbol": "♃", "angle": 280},
    {"name": "Saturn", "symbol": "♄", "angle": 315},
    {"name": "Uranus", "symbol": "♅", "angle": 150},
    {"name": "Neptune", "symbol": "♆", "angle": 240},
    {"name": "Pluto", "symbol": "♇", "angle": 330}
]

# Draw outer circle
theta_circle = np.linspace(0, 2*np.pi, 100)
x_outer = np.cos(theta_circle)
y_outer = np.sin(theta_circle)

fig.add_trace(go.Scatter(x=x_outer, y=y_outer, mode='lines',
                         line=dict(color='white', width=3),
                         showlegend=False, hoverinfo='skip'))

# Draw inner circle for houses
x_inner = 0.7 * np.cos(theta_circle)
y_inner = 0.7 * np.sin(theta_circle)

fig.add_trace(go.Scatter(x=x_inner, y=y_inner, mode='lines',
                         line=dict(color='white', width=2),
                         showlegend=False, hoverinfo='skip'))

# Draw zodiac sign sectors with colors
for i, sign in enumerate(zodiac_signs):
    # Each sign spans 30 degrees
    start_angle = i * 30
    end_angle = (i + 1) * 30
    
    # Convert to radians (starting from 0° at right, going counterclockwise)
    theta_start = np.radians(start_angle)
    theta_end = np.radians(end_angle)
    
    # Create sector points
    theta_sector = np.linspace(theta_start, theta_end, 20)
    r_outer = 1.0
    r_inner = 0.85
    
    # Outer arc
    x_arc_outer = r_outer * np.cos(theta_sector)
    y_arc_outer = r_outer * np.sin(theta_sector)
    
    # Inner arc (reversed)
    x_arc_inner = r_inner * np.cos(theta_sector[::-1])
    y_arc_inner = r_inner * np.sin(theta_sector[::-1])
    
    # Combine to create closed shape
    x_sector = np.concatenate([x_arc_outer, x_arc_inner, [x_arc_outer[0]]])
    y_sector = np.concatenate([y_arc_outer, y_arc_inner, [y_arc_outer[0]]])
    
    fig.add_trace(go.Scatter(
        x=x_sector, y=y_sector,
        fill='toself',
        fillcolor=sign['color'],
        opacity=0.3,
        line=dict(color=sign['color'], width=1),
        showlegend=False,
        hoverinfo='skip'
    ))
    
    # Add zodiac symbol
    mid_angle = (start_angle + end_angle) / 2
    theta_mid = np.radians(mid_angle)
    x_text = 0.925 * np.cos(theta_mid)
    y_text = 0.925 * np.sin(theta_mid)
    
    fig.add_annotation(
        x=x_text, y=y_text,
        text=sign['symbol'],
        showarrow=False,
        font=dict(size=20, color='white'),
        xanchor='center',
        yanchor='middle'
    )

# Draw 12 house division lines (Placidus style)
for i in range(12):
    angle = i * 30
    theta = np.radians(angle)
    
    x_line = [0.7 * np.cos(theta), 1.0 * np.cos(theta)]
    y_line = [0.7 * np.sin(theta), 1.0 * np.sin(theta)]
    
    fig.add_trace(go.Scatter(x=x_line, y=y_line, mode='lines',
                             line=dict(color='black', width=2),
                             showlegend=False, hoverinfo='skip'))

# Add main angles (ASC, MC, DSC, IC) with labels
# ASC at 180° (9 o'clock), MC at 90° (12 o'clock), DSC at 0° (3 o'clock), IC at 270° (6 o'clock)
angles_points = [
    {"name": "ASC", "angle": 180, "color": "white"},
    {"name": "MC", "angle": 90, "color": "white"},
    {"name": "DSC", "angle": 0, "color": "white"},
    {"name": "IC", "angle": 270, "color": "white"}
]

for point in angles_points:
    theta = np.radians(point['angle'])
    x_line = [0, 1.15 * np.cos(theta)]
    y_line = [0, 1.15 * np.sin(theta)]
    
    fig.add_trace(go.Scatter(x=x_line, y=y_line, mode='lines',
                             line=dict(color=point['color'], width=3),
                             showlegend=False, hoverinfo='skip'))
    
    # Add label
    x_text = 1.25 * np.cos(theta)
    y_text = 1.25 * np.sin(theta)
    
    fig.add_annotation(
        x=x_text, y=y_text,
        text=point['name'],
        showarrow=False,
        font=dict(size=16, color='white', family='Arial Black'),
        xanchor='center',
        yanchor='middle'
    )

# Add planets with symbols
for planet in planets:
    theta = np.radians(planet['angle'])
    r = 0.5  # Position inside the inner circle
    
    x_planet = r * np.cos(theta)
    y_planet = r * np.sin(theta)
    
    # Add planet symbol
    fig.add_annotation(
        x=x_planet, y=y_planet,
        text=planet['symbol'],
        showarrow=False,
        font=dict(size=18, color='#D2BA4C'),
        xanchor='center',
        yanchor='middle'
    )

# Update layout
fig.update_layout(
    title={
        "text": "Natal Chart - Cosmogram<br><span style='font-size: 18px; font-weight: normal;'>Traditional astrological wheel with houses and planets</span>",
        "x": 0.5,
        "xanchor": "center"
    },
    showlegend=False,
    xaxis=dict(
        showgrid=False,
        showticklabels=False,
        zeroline=False,
        range=[-1.4, 1.4],
        scaleanchor="y",
        scaleratio=1
    ),
    yaxis=dict(
        showgrid=False,
        showticklabels=False,
        zeroline=False,
        range=[-1.4, 1.4]
    ),
    plot_bgcolor='#0a0a0a',
    paper_bgcolor='#0a0a0a',
    font=dict(color='white')
)

# Save the chart
try:
    # Попытка сохранить как изображение (требует kaleido)
    fig.write_image("natal_chart.png")
    print("✅ Изображение сохранено: natal_chart.png")
except Exception as e:
    print(f"⚠️  Не удалось сохранить PNG (возможно, не установлен kaleido): {e}")
    print("   Установите: pip install kaleido")
    print("   Или используйте HTML версию ниже")

try:
    fig.write_image("natal_chart.svg", format="svg")
    print("✅ SVG сохранено: natal_chart.svg")
except Exception as e:
    print(f"⚠️  Не удалось сохранить SVG: {e}")

# Всегда сохраняем HTML версию (не требует kaleido)
try:
    fig.write_html("natal_chart.html")
    print("✅ HTML версия сохранена: natal_chart.html")
except Exception as e:
    print(f"❌ Ошибка при сохранении HTML: {e}")
