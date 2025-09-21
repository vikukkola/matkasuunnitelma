from PIL import Image, ImageDraw, ImageEnhance
import random, math

# --- Config ---
input_jpeg = "cover.JPEG"
output_jpeg = "lightened_hearts.jpg"

# --- Step 1: Load image ---
image = Image.open(input_jpeg).convert("RGB")

# --- Step 2: Lighten image ---
enhancer = ImageEnhance.Brightness(image)
image = enhancer.enhance(1.7)  # >1.0 = brighter, <1.0 = darker

# --- Step 3: Draw hearts ---
draw = ImageDraw.Draw(image)

# --- Step 4: Save result ---
image.save(output_jpeg)
print(f"✅ Lightened image with hearts saved as '{output_jpeg}'")
