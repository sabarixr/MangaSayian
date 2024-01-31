import os
import pdf_maker
so_rted = os.listdir("dwnloaded_images")
x=so_rted
em_pt = []
for _ in range(len(so_rted)):
    for ___ in so_rted: 
        __ = ___[:-4]
        if __ ==str(_):
            
            em_pt.append(___)
print(em_pt)
my_dict = {i: value for i, value in enumerate(em_pt)}
pdf_maker.create_pdf(my_dict)