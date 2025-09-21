from PIL import Image, ImageDraw
import random, math

# --- Config ---
input_jpeg = "lightened_hearts.jpg"   # your photo
output_gif = "pulsating_hearts.gif"

num_frames = 20      # frames for one pulse cycle
hearts_count = 15    # how many hearts to animate
size_range = (1, 12) # min/max heart size

# --- Load background ---
base_img = Image.open(input_jpeg).convert("RGB")

# --- Create fixed heart positions ---
hearts = []
for _ in range(hearts_count):
    x = random.randint(50, base_img.width - 50)
    y = random.randint(50, base_img.height - 50)
    base_size = random.randint(*size_range)
    hearts.append((x, y, base_size))

# --- Heart drawing function ---
def draw_heart(draw, x, y, size, color):
    """Draw a heart using parametric equation."""
    points = []
    for t in range(0, 360, 5):
        angle = math.radians(t)
        xh = size * 16 * math.sin(angle) ** 3
        yh = -size * (13 * math.cos(angle) - 5 * math.cos(2 * angle)
                      - 2 * math.cos(3 * angle) - math.cos(4 * angle))
        points.append((x + xh, y + yh))
    draw.polygon(points, fill=color)

# --- Generate animation frames ---
frames = []
for frame in range(num_frames):
    # fresh copy of background
    img = base_img.copy()
    draw = ImageDraw.Draw(img)

    # pulsating effect (sinusoidal scaling)
    scale = 1 + 0.3 * math.sin(2 * math.pi * frame / num_frames)

    for (x, y, base_size) in hearts:
        size = int(base_size * scale)
        color = (255, 0, 80)  # romantic red-pink
        draw_heart(draw, x, y, size, color)

    frames.append(img)

# --- Save animated GIF ---
frames[0].save(output_gif,
               save_all=True,
               append_images=frames[1:],
               duration=100,  # ms per frame
               loop=0)

print(f"✅ Saved animated GIF as '{output_gif}'")
