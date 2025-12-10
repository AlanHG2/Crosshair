import cairo
import math

# Parámetros
width, height = 100, 100
center_x, center_y = width / 2, height / 2
outer_radius = 10
inner_radius = 2
line_length = 6
angles_deg = [45, 135, 225, 315]

# Crear surface transparente
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
ctx = cairo.Context(surface)
ctx.set_antialias(cairo.ANTIALIAS_BEST)

# Fondo transparente
ctx.set_source_rgba(0, 0, 0, 0)
ctx.paint()

# Segmentos de círculo grande (naranja) en las esquinas
ctx.set_source_rgb(0, 0.788, 0.314)  # Naranja
ctx.set_line_width(1)
arc_span = math.radians(45)  # Cada segmento abarca 45 grados
for angle_deg in angles_deg:
    angle_rad = math.radians(angle_deg)
    start_angle = angle_rad - arc_span / 2
    end_angle = angle_rad + arc_span / 2
    ctx.arc(center_x, center_y, outer_radius, start_angle, end_angle)
    ctx.stroke()

# Círculo pequeño (rojo) completo en el centro
ctx.set_source_rgb(0.925, 0, 0.247)  # Rojo
ctx.arc(center_x, center_y, inner_radius, 0, 2 * math.pi)
ctx.fill()

# Líneas a 45°
# ctx.set_source_rgb(0, 0.7, 0)  # Negro
# ctx.set_line_width(1)
# for angle_deg in angles_deg:
#     angle_rad = math.radians(angle_deg)
#     x1 = center_x + outer_radius * math.cos(angle_rad)
#     y1 = center_y + outer_radius * math.sin(angle_rad)
#     x2 = x1 - line_length * math.cos(angle_rad)
#     y2 = y1 - line_length * math.sin(angle_rad)
#     ctx.move_to(x1, y1)
#     ctx.line_to(x2, y2)
#     ctx.stroke()

# Exportar PNG
surface.write_to_png("Crosshair7.png")
