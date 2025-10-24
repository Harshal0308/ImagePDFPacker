
import os
import random
import numpy as np
from PIL import Image, ImageDraw

def generate_random_images(output_dir="input_images", num_images=10):
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i in range(num_images):
        width = random.randint(100, 500)
        height = random.randint(100, 500)
     
        image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)
        
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255)
        

        shape_type = random.choice(["rectangle", "ellipse", "polygon"])
        
        if shape_type == "rectangle":
            x0 = random.randint(0, width // 2)
            y0 = random.randint(0, height // 2)
            x1 = random.randint(x0 + 20, width)
            y1 = random.randint(y0 + 20, height)
            draw.rectangle([x0, y0, x1, y1], fill=color)
        elif shape_type == "ellipse":
            x0 = random.randint(0, width // 2)
            y0 = random.randint(0, height // 2)
            x1 = random.randint(x0 + 20, width)
            y1 = random.randint(y0 + 20, height)
            draw.ellipse([x0, y0, x1, y1], fill=color)
        elif shape_type == "polygon":
            num_points = random.randint(3, 8)
            points = []
            for _ in range(num_points):
                points.append((random.randint(0, width), random.randint(0, height)))
            draw.polygon(points, fill=color)
     
        image.save(os.path.join(output_dir, f"random_image_{i+1}.png"))

    print(f"Generated {num_images} random images in '{output_dir}'")

if __name__ == "__main__":
    generate_random_images()
