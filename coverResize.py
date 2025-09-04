import os
from PIL import Image

MAX_SIZE = (500, 500)

def resize_cover(path):
    try:
        with Image.open(path) as img:
            width, height = img.size
            if width > 500 or height > 500:
                print(f"Resizing: {path} ({width}x{height}) -> max 500x500 (maintaining aspect ratio)")
                img.thumbnail(MAX_SIZE, Image.LANCZOS)
                img.save(path)
            else:
                print(f"Skipping (already <= 500x500): {path} ({width}x{height})")
    except Exception as e:
        print(f"Error processing {path}: {e}")

def main():
    for root, _, files in os.walk("."):
        for file in files:
            if file.lower() in ("cover.jpg", "cover.png"):
                resize_cover(os.path.join(root, file))

if __name__ == "__main__":
    main()
