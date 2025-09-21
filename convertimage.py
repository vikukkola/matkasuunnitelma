from PIL import Image, ImageDraw
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import random, math

# --- Step 1: Load JPEG image ---
input_jpeg = "cover.jpg"   # your input photo
output_jpeg = "cover_hearts_added.jpg"
output_pdf  = "cover_hearts_pdf.pdf"

image = Image.open(input_jpeg).convert("RGB")
draw = ImageDraw.Draw(image)

# --- Step 2: Heart drawing function ---
def draw_heart(draw, x, y, size, color):
    """Draw a heart shape using a parametric equation."""
    points = []
    for t in range(0, 360, 5):
        angle = math.radians(t)
        xh = size * 16 * math.sin(angle) ** 3
        yh = -size * (13 * math.cos(angle) - 5 * math.cos(2 * angle)
                      - 2 * math.cos(3 * angle) - math.cos(4 * angle))
        points.append((x + xh, y + yh))
    draw.polygon(points, fill=color)

# --- Step 3: Add random hearts to the JPEG ---
for _ in range(25):  # number of hearts
    x = random.randint(50, image.width - 50)
    y = random.randint(50, image.height - 50)
    size = random.randint(8, 25)
    color = (255, 0, 80)  # romantic red-pink
    draw_heart(draw, x, y, size, color)

# Save modified JPEG
image.save(output_jpeg)

# --- Step 4: Embed into PDF using ReportLab ---
c = canvas.Canvas(output_pdf, pagesize=letter)
page_width, page_height = letter

# Scale image to fit page if larger
img_width, img_height = image.size
scale = min(page_width / img_width, page_height / img_height) * 0.95
final_width = img_width * scale
final_height = img_height * scale

x_offset = (page_width - final_width) / 2
y_offset = (page_height - final_height) / 2

c.drawImage(output_jpeg, x_offset, y_offset, final_width, final_height)
c.save()

print(f"✅ Done! Saved modified image as '{output_jpeg}' and embedded into PDF '{output_pdf}'.")
