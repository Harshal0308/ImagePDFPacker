import os
import argparse
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.utils import ImageReader


from rectpack import newPacker, PackingMode

class Packer:
    def __init__(self, page_width, page_height):
        self.page_width = page_width
        self.page_height = page_height
        self.pages = []

    def pack(self, images):
        packer = newPacker(mode=PackingMode.Offline)

        for i, img_data in enumerate(images):
            packer.add_rect(*img_data['size'], rid=i)

        packer.add_bin(self.page_width, self.page_height, count=float('inf'))
        
        packer.pack()

        num_pages = len(packer)
        self.pages = [[] for _ in range(num_pages)]

        for rect in packer.rect_list():
            page_index, x, y, w, h, img_index = rect
            img_path = images[img_index]['path']
            self.pages[page_index].append({
                'path': img_path,
                'pos': (x, y),
                'size': (w, h)
            })

def preprocess_image(image_path, page_width, page_height):
    
    try:
        with Image.open(image_path) as img:
            if img.mode == 'RGBA':
                bbox = img.getbbox()
                if bbox:
                    img = img.crop(bbox)

            width, height = img.size
            if width > page_width or height > page_height:
                ratio = min(page_width/width, page_height/height)
                new_width = int(width * ratio)
                new_height = int(height * ratio)
                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            return img, img.size
    except (IOError, Image.UnidentifiedImageError) as e:
        print(f"Warning: Could not process image {image_path}: {e}")
        return None, (0, 0)

def main():
    parser = argparse.ArgumentParser(description="Pack images into a PDF.")
    parser.add_argument("--input", default="input_images", help="Folder with images to pack.")
    parser.add_argument("--output", default="output.pdf", help="Output PDF file.")
    parser.add_argument("--page-size", default="A4", choices=["A4", "Letter"], help="PDF page size.")
    args = parser.parse_args()

    if not os.path.isdir(args.input):
        print(f"Error: Input directory '{args.input}' not found.")
        return

    image_files = [os.path.join(args.input, f) for f in os.listdir(args.input) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    if not image_files:
        print(f"Error: No PNG or JPG images found in '{args.input}'.")
        return

    print(f"Found {len(image_files)} images to process...")

    page_size = A4 if args.page_size == "A4" else letter
    page_width, page_height = page_size

    processed_images = []
    total_image_area = 0
    for img_path in image_files:
        _, size = preprocess_image(img_path, page_width, page_height)
        if size[0] > 0 and size[1] > 0:
            processed_images.append({'path': img_path, 'size': size})
            total_image_area += size[0] * size[1]

    packer = Packer(page_width, page_height)
    packer.pack(processed_images)

    # Create PDF
    c = canvas.Canvas(args.output, pagesize=page_size)
    for i, page_images in enumerate(packer.pages):
        if i > 0:
            c.showPage()
        for img_info in page_images:
            img_path = img_info['path']
            x, y = img_info['pos']
            w, h = img_info['size']

            c.drawImage(ImageReader(img_path), x, y, width=w, height=h, mask='auto')
    c.save()

    num_pages = len(packer.pages)
    total_pdf_area = num_pages * page_width * page_height
    wasted_space = 1 - (total_image_area / total_pdf_area)

    print(f"\nPDF generation complete: '{args.output}'")
    print("--- Layout Statistics ---")
    print(f"Total images packed: {len(processed_images)}")
    print(f"Pages used: {num_pages}")
    print(f"Wasted space: {wasted_space:.2%}")

if __name__ == "__main__":
    main()