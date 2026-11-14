import os
import subprocess
import sys

# Automatically install Pillow if missing
try:
    from PIL import Image, ImageOps
except ImportError:
    print("Pillow not found. Installing Pillow...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image, ImageOps

VALID_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.webp'}

def compress_images():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(base_dir, 'images')

    if not os.path.isdir(images_dir):
        print(f"Directory not found: {images_dir}")
        return

    compressed_count = 0
    saved_bytes = 0

    for root, _, files in os.walk(images_dir):
        rel_root = os.path.relpath(root, images_dir)
        is_member = 'members' in rel_root.split(os.sep)
        max_width = 600 if is_member else 1600

        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext not in VALID_EXTENSIONS:
                continue

            filepath = os.path.join(root, file)
            initial_size = os.path.getsize(filepath)

            try:
                with Image.open(filepath) as img:
                    # Correct orientation based on EXIF before stripping metadata
                    img = ImageOps.exif_transpose(img)

                    # Resize if width exceeds max_width
                    if img.width > max_width:
                        new_width = max_width
                        new_height = int(round(img.height * (new_width / img.width)))
                        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

                    # Save in place without metadata at 80% quality
                    if ext in {'.jpg', '.jpeg'}:
                        if img.mode in ('RGBA', 'P'):
                            img = img.convert('RGB')
                        img.save(filepath, 'JPEG', quality=80, optimize=True)
                    elif ext == '.png':
                        img.save(filepath, 'PNG', optimize=True)
                    elif ext == '.webp':
                        img.save(filepath, 'WEBP', quality=80, optimize=True)

                final_size = os.path.getsize(filepath)
                saved_bytes += max(0, initial_size - final_size)
                compressed_count += 1
                print(f"Compressed: {os.path.relpath(filepath, base_dir)} ({initial_size // 1024} KB -> {final_size // 1024} KB)")
            except Exception as e:
                print(f"Error compressing {filepath}: {e}")

    print(f"\nCompleted! Processed {compressed_count} images. Total space saved: {saved_bytes / 1024 / 1024:.2f} MB")

if __name__ == '__main__':
    compress_images()
