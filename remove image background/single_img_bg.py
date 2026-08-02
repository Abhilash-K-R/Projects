from rembg import remove
from PIL import Image

input_path = " "  # input image path
output_path = " "  # output image path

input_image = Image.open(input_path)
output_image = remove(input_image)
output_image.save(output_path)

print("Done!")
