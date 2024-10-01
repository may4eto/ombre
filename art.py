from PIL import Image
import os

def make_art(filepath):
    img = Image.new("RGBA", size=(500, 500), color=(255, 255, 0, 255))
    img.save(filepath)

if __name__ == "__main__":
    print("Run art.py")
    os.makedirs("test", exist_ok=True)
    filepath = os.path.join("test", "art.png")
    make_art(filepath)