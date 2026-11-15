import os
import subprocess
import sys

# Auto-install Pillow if missing
try:
    from PIL import Image, ImageOps
except ImportError:
    print("Pillow not found. Installing Pillow...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image, ImageOps

VALID_EXTENSIONS = {'.jpg', '.jpeg', '.png'}

def get_folder_size(folder):
    total = 0
    for root, _, files in os.walk(folder):
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in VALID_EXTENSIONS:
                total += os.path.getsize(os.path.join(root, f))
    return total

def compress_images():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(base_dir, 'images')

    if not os.path.isdir(images_dir):
        print(f"Error: Directory not found: {images_dir}")
        return

    initial_total_size = get_folder_size(images_dir)
    print(f"Scanning images in: {images_dir}")
    print(f"Initial total images size: {initial_total_size / (1024 * 1024):.2f} MB\n")
    print(f"{'Filename':<55} | {'Old Size':<10} | {'New Size':<10} | {'Status'}")
    print("-" * 90)

    processed = 0

    for root, _, files in os.walk(images_dir):
        rel_root = os.path.relpath(root, images_dir)
        is_member = 'members' in rel_root.lower().split(os.sep)

        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext not in VALID_EXTENSIONS:
                continue

            filepath = os.path.join(root, file)
            rel_file = os.path.relpath(filepath, images_dir).replace('\\', '/').lower()
            
            if rel_file in ('logo.jpeg', 'logo.jpg'):
                max_width = 300
            elif is_member:
                max_width = 400
            else:
                max_width = 1000

            old_size = os.path.getsize(filepath)

            try:
                with Image.open(filepath) as img:
                    img = ImageOps.exif_transpose(img)

                    # Resize preserving aspect ratio
                    if img.width > max_width:
                        new_width = max_width
                        new_height = int(round(img.height * (new_width / img.width)))
                        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

                    # Overwrite in place cleanly without metadata
                    if ext in {'.jpg', '.jpeg'}:
                        if img.mode in ('RGBA', 'P'):
                            img = img.convert('RGB')
                        img.save(filepath, 'JPEG', quality=72, optimize=True, progressive=True)
                    elif ext == '.png':
                        img.save(filepath, 'PNG', optimize=True)

                new_size = os.path.getsize(filepath)
                rel_path = os.path.relpath(filepath, base_dir)
                diff = old_size - new_size
                status = f"-{diff // 1024} KB" if diff > 0 else ("0 KB" if diff == 0 else f"+{abs(diff) // 1024} KB")

                print(f"{rel_path:<55} | {old_size / 1024:>7.1f} KB | {new_size / 1024:>7.1f} KB | {status}")
                processed += 1

            except Exception as e:
                print(f"Error processing {file}: {e}")

    final_total_size = get_folder_size(images_dir)
    total_saved = initial_total_size - final_total_size

    print("-" * 90)
    print(f"Total processed files: {processed}")
    print(f"Before compression   : {initial_total_size / (1024 * 1024):.2f} MB ({initial_total_size:,} bytes)")
    print(f"After compression    : {final_total_size / (1024 * 1024):.2f} MB ({final_total_size:,} bytes)")
    print(f"Total size reduced   : {total_saved / (1024 * 1024):.2f} MB ({total_saved:,} bytes)")

if __name__ == '__main__':
    compress_images()
