import os
from rembg import remove
from PIL import Image

input_folder = "remove image background/input_images"
output_folder = "remove image background/output_images"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Supported image formats
extensions = (".jpg", ".jpeg", ".png", ".webp")

for filename in os.listdir(input_folder):

    if filename.lower().endswith(extensions):

        input_path = os.path.join(input_folder, filename)

        # Save as PNG (transparent background)
        output_name = os.path.splitext(filename)[0] + ".png"
        output_path = os.path.join(output_folder, output_name)

        image = Image.open(input_path)
        output = remove(image)
        output.save(output_path)

        print(f"Processed: {filename}")

print("All images completed!")
