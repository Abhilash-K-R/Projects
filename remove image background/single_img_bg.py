from rembg import remove
from PIL import Image

input_path = "remove image background/dodge.jpeg"
output_path = "photo_no_bg.png"

input_image = Image.open(input_path)
output_image = remove(input_image)
output_image.save(output_path)

print("Done!")
