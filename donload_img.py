import os
import requests
from pdf_maker import create_pdf
def download_images(image_links ):
    
    if not os.path.exists('dwnloaded_images'):
        os.makedirs('dwnloaded_images')
    else:
        for filename in os.listdir('dwnloaded_images'):
            file_path = os.path.join('dwnloaded_images', f'{filename}.png')
            if os.path.isfile(file_path):
                os.remove(file_path)

    links___ = []
    for i, link in enumerate(image_links, 1):
        link = link.strip()  
        filename = os.path.join('dwnloaded_images', f'{str(i)}.jpg')
        response = requests.get(link)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
                links___.append(response.content)
            print(f"Downloaded {filename}")
        else:
            print(f"Failed to download {link}")

    print(links___)