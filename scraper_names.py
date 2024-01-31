import requests
from bs4 import BeautifulSoup as soup
from fuzzywuzzy import fuzz
import os
from scraper_pages import img_downloader

similar_names ={}

url = 'https://asuratoon.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    sp_page = soup(response.content, 'html.parser')
    new_rl = sp_page.find_all('div', class_ = "luf")
    for _ in new_rl:
        print(_.text)
    search_book= input("Enter the book you wanna dowland : ")
    i=0
    for _ in new_rl:
        names__= new_rl[i].find('h4')        
        if (fuzz.ratio(names__.text, search_book)) >70:
            similar_names[i] = names__.text
        i= i+1

    print(similar_names)
    print(f"the book you are searching is  yes/no?")
    inp = input("Yes/No ")
    if inp == "No":
        os.exit()
    
    
    chapter_no = input("Chapter Number: ")
    for index,name in similar_names.items():
        if name == search_book:
            break
    if (new_rl[index].find('ul').find_all('a'))[0].get_text(strip=True).endswith(chapter_no):
        link_chapt = ((new_rl[index].find('ul').find_all('a'))[0])['href']
    else:
        link_chapt = ((new_rl[index].find('ul').find_all('a'))[1])['href']
        link_chapt = (link_chapt.rsplit('-', 1))[0] +'-'+ chapter_no+ '/'
    print(link_chapt)
    img_downloader(link_chapt)
else:
    print(f"Failed to access the website. Status code: {response.status_code}")
