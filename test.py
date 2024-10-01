import os
from art import make_art

os.makedirs("test", exist_ok=True)

print("Generating images...")

for i in range(1, 11):
    filepath = os.path.join("test", f"test-{i}.png")
    make_art(filepath)

