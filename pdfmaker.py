from fpdf import FPDF
import os

pdf = FPDF()
pdf.set_auto_page_break(0)
img_list = os.listdir('dwnloaded_images')
sorted_list = []
for _ in range(len(img_list)):
    for ___ in img_list: 
        __ = ___[:-4]
        if __ ==str(_):
            
            sorted_list.append(___)

for image in sorted_list:
    pdf.add_page()
    pdf.image(f"dwnloaded_images/{image}", 0, 0, 210, 297)

pdf.output("manga.pdf")