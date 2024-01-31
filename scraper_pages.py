from selenium import webdriver
from bs4 import BeautifulSoup
from donload_img import download_images
def img_downloader(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode to hide the browser window
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        
        # Let the page load for a few seconds to allow dynamic content to be loaded
        driver.implicitly_wait(5)
        
        # Get the page source after dynamic content has loaded
        html_source = driver.page_source
        
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(html_source, 'html.parser')
        fetched_ = soup
        print(fetched_)
        print("\n\n\n\n\n\n\n")
        img_tags = soup.find_all('img', {'alt': 'asura scans manhwa comic'})
        print(img_tags)
        links__= []
        with open("img.txt", "w") as file:
            for img_tag in img_tags:
                img_url = img_tag['src']
                links__.append(img_url)
                file.write(img_url + '\n')
        download_images(links__)
    finally:
        driver.quit()
