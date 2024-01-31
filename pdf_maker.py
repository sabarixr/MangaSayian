from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image
import os

def crop_image(image_path, output_path, crop_percentage):
    img = Image.open(image_path)
    width, height = img.size
    crop_pixels = int(width * crop_percentage)

    # Crop the image equally from both sides
    img = img.crop((crop_pixels, 0, width - crop_pixels, height))
    img.save(output_path)

def create_pdf(images):
    c = canvas.Canvas("output.pdf", pagesize=letter)

    # Add images to PDF
    for i, (index, image_path) in enumerate(images.items(), 1):
        if i == 3:  # Apply cropping to the 3rd image
            crop_percentage = 0.3
            cropped_image_path = f"cropped_{index}.png"
            crop_image(image_path, cropped_image_path, crop_percentage)
            c.drawImage(cropped_image_path, 50, 50, width=400, height=400)
        else:
            c.drawImage(image_path, 50, 50, width=400, height=400)

        c.showPage()

    c.save()



