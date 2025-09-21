from PIL import Image, ImageDraw
import random
import math

# Load background image
image = Image.open("cover.jpg").convert("RGB")
draw = ImageDraw.Draw(image)

def draw_heart(draw, x, y, size, color):
    """Draw a simple heart shape using polygon approximation."""
    points = []
    for t in range(0, 360, 5):
        angle = math.radians(t)
        # Parametric heart equation
        xh = size * 16 * math.sin(angle) ** 3
        yh = -size * (13 * math.cos(angle) - 5 * math.cos(2 * angle)
                      - 2 * math.cos(3 * angle) - math.cos(4 * angle))
        points.append((x + xh, y + yh))
    draw.polygon(points, fill=color)

# Draw random hearts
for _ in range(20):
    x = random.randint(50, image.width - 50)
    y = random.randint(50, image.height - 50)
    size = random.randint(5, 20)
    color = (255, 0, 80)  # Romantic red-pink
    draw_heart(draw, x, y, size, color)

# Save new image
image.save("cover.jpg")
