from art import Artwork
import os
from PIL import Image, ImageDraw

print("generating images")

os.makedirs("exports", exist_ok=True)

filepath = os.path.join("exports", "export.png")

chosen_image = Image.open(r"/Users/mayamircheva/Downloads/ombre/test/circles-1.png") 
art = chosen_image.resize((2000, 2000))

# art = Artwork((2000, 2000))
art.save(filepath)