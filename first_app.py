from selenium import webdriver
from bs4 import BeautifulSoup
from flask import Flask
from uuid import uuid4
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('manga_links.db',check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS manga_links (
        id TEXT PRIMARY KEY,
        link TEXT
    )
''')
conn.commit()

@app.route('/')
def hello_world():
    return '<center><b>Hello, World!<b><center>'

def img_scraper(url):
    global cursor, conn
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    n = str(uuid4())
    links__ = []
    driver.get(url)
    driver.implicitly_wait(10)
    html_source = driver.page_source
    soup = BeautifulSoup(html_source, 'html.parser')
    img_tags = soup.find_all('img')

    for img_tag in img_tags:
        img_url = img_tag['src']
        if img_url.endswith(".png"):
            continue
        links__.append(img_url)
    print(links__)
    cursor.execute("INSERT INTO manga_links (id, link) VALUES (?, ?)", (n, ','.join(links__)))
    conn.commit()

    driver.quit()
    return f"http://127.0.0.1:5000/view/{n}"

@app.route("/manga/")
def manga():
    url = "https://asuratoon.com/9643503911-omniscient-readers-viewpoint-chapter-1/"
    return img_scraper(url)

@app.route("/view/<spec_key>")
def view_manga(spec_key):
    global cursor
    cursor.execute("SELECT link FROM manga_links WHERE id=?", (spec_key,))
    result = cursor.fetchone()
    if result:
        links = result[0].split(',')
        html = "<center>"
        for link in links:
            html += f"<img src='{link}'><br>"
        html += "</center>"
        return html
    else:
        return "Page not found."

if __name__ == "__main__":
    app.run()
