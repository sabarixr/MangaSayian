from selenium import webdriver
from bs4 import BeautifulSoup
from flask import Flask
from uuid import uuid4
import threading
import time

app = Flask(__name__)
link_dir = {}


@app.route('/')
def hello_world():
    return '<center><b>Hello, World!<b><center>'


def img_scraper(title, chapter):
    converted_title = title.lower().replace(" ", "-").replace("’", "")
    url = f"https://asuratoon.com/9643503911-{converted_title}-chapter-{chapter}/"
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    n = str(uuid4())
    try:
        driver.get(url)
        driver.implicitly_wait(5)
        html_source = driver.page_source
        soup = BeautifulSoup(html_source, 'html.parser')
        img_tags = soup.find_all('img', {'alt': 'asura scans manhwa comic'})
        links__ = []
        for img_tag in img_tags:
            img_url = img_tag['src']
            if img_url.endswith(".png"):
                continue
            links__.append(img_url)
            link_dir[n] = links__

        threading.Thread(target=remove_link_after_delay, args=(n, 14400)).start()
    except Exception as e:
        print(f'{e} the webpage was not found')
    finally:
        driver.quit()
    return f"http://127.0.0.1:5000/view/{n}"


def remove_link_after_delay(key, delay):
    time.sleep(delay)
    if key in link_dir:
        del link_dir[key]



def BooksHosted():
    return "Books hosted on this server: " + str(len(link_dir))


@app.route("/view/<spec_key>")
def view_manga(spec_key):
    print(str(BooksHosted()))
    if spec_key in link_dir:
        links = link_dir[spec_key]
        html = "<center>"
        for link in links:
            html += f"<img src='{link}'><br>"
        html += "</center>"
        return html
    else:
        return "Page not found."


if __name__ == "__main__":
    app.run()
