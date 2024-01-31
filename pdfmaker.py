from fpdf import FPDF
import os

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
img_list = os.listdir('dwnloaded_images')
img_list.sort(key=lambda x: int(os.path.splitext(x)[0]))

for image in img_list:
    if image.endswith('.png'):
        pdf.add_page()
        try:
            pdf.image(f"dwnloaded_images/{image}", x=14, y=15, w=500)
        except Exception as e:
            print(f"Error adding {image}:", e)

pdf.output("manga.pdf")
