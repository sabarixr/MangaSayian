import requests
from bs4 import BeautifulSoup as soup

def scraper_detailed(name):
    title = (name.lstrip("/link").strip()).lower().replace(" ", "-").replace("’", "")
    url = f"https://asuratoon.com/manga/5588556462-{title}/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        result_ = soup(response.content, 'html.parser')
    else:
        result_ = f"Error: {response.status_code}"

    return result_

def check_scrap(name):
    print(name)
    out_n= "```\n Chapter : date released"
    data = scraper_detailed(name)
    new_up= data.find_all('div', {'class': 'chbox'})
    for item in new_up:
        ch_title = item.find('span').text.strip()
        ch_link = item.find_all('span')[1].text.strip()
        out_n += f"{ch_title} : {ch_link}\n"
    out_n+= "```"

    return out_n
    print(out_n)

def info_scrap(name):
    out = ""
    data = scraper_detailed(name)
    title = data.find('h1', {'class': 'entry-title'}).text.strip() 
    info = data.find("p")
    author = data.find_all('div', class_ = "fmed")[1].find('span').text.strip()
    out = f"```{title}\n\n{info.text}\n\nAuthor: {author}```"
    return out

    
#check_scrap("Solo leveling")