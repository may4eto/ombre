from art import make_art
import os

os.makedirs("exports", exist_ok=True)

print("Generating images...")

filepath = os.path.join("exports", "export.png")

make_art(filepath, (2000, 2000))