import requests
from bs4 import BeautifulSoup as soup

def scraper_splash():
    url = 'https://asuratoon.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        result_ = soup(response.content, 'html.parser')
    else:
        result_ = f"Error: {response.status_code}"

    return result_




def get_names():
    result = ""
    scrapped = scraper_splash()
    
        

    new_rl = scrapped.find_all('div', class_="luf")
    result += "```" 
    for i in new_rl:
        #while nos< 5:
            if len(result)> 1000:
                break
            h4_text = i.find('h4').text.strip()
            a_text = i.find('a').text.strip()
            span_text = i.find('span').text.strip()
            result += f"Title: {h4_text}\n"
            result += f"Chapter: {a_text}\n"
            result += f"Published: {span_text}\n\n"
        #nos+=1
    result += "```" 
    return result

def get_top():
    top_result = ''
    scrapped_page = scraper_splash()
    top_list = scrapped_page.find_all('div', class_="leftseries")
    nos = 0
    top_result += "```"
    for item in  top_list:
        if nos < 5:
            name = item.find('a').text.strip()
            top_result +=  f'{nos+1}. {name}\n'
            geans =  "  > "+', '.join([f'{a_tag.text.strip()}' for span_tag in item.find_all('span') for a_tag in span_tag.find_all('a')])
            top_result += f'{geans}\n'
            top_result+= '\n'
        nos +=1
    top_result += "```"   
    return top_result