from PIL import Image
import os


def convert_jpg_to_png(input_path, output_path):
    # Open the image file
    with Image.open(input_path) as img:
        # Convert image to PNG
        img.save(output_path, 'PNG')


# Example usage
input_path = "astro.jpg"
output_path = 'astro.png'
convert_jpg_to_png(input_path, output_path)
