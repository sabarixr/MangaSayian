import os
import requests

def download_images(image_links ):
    # Create the 'dwnloaded_images' if it doesn't exist
    if not os.path.exists('dwnloaded_images'):
        os.makedirs('dwnloaded_images')
    else:
        # If 'dwnloaded_images' exists, delete existing files
        for filename in os.listdir('dwnloaded_images'):
            file_path = os.path.join('dwnloaded_images', f'{filename}.png')
            if os.path.isfile(file_path):
                os.remove(file_path)

    # Download images and save them as 1.svg, 2.svg, 3.svg, ...
    for i, link in enumerate(image_links, 1):
        link = link.strip()  # Remove leading/trailing whitespace
        filename = os.path.join('dwnloaded_images', f'{str(i)}.png')
        response = requests.get(link)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded {filename}")
        else:
            print(f"Failed to download {link}")