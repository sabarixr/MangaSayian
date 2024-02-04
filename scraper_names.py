import requests
from bs4 import BeautifulSoup as soup

def get_names():
    result = ""

    url = 'https://asuratoon.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        sp_page = soup(response.content, 'html.parser')
        new_rl = sp_page.find_all('div', class_="luf")

        for i in new_rl:
            h4_text = i.find('h4').text.strip()
            a_text = i.find('a').text.strip()
            span_text = i.find('span').text.strip()

            result += f"Title: {h4_text}\n"
            result += f"Chapter: {a_text}\n"
            result += f"Published: {span_text}\n\n"

    else:
        result = f"Error: {response.status_code}"

    return result

