import requests
from bs4 import BeautifulSoup as soup

def scraper_splash(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        result_ = soup(response.content, 'html.parser')
    else:
        result_ = f"Error: {response.status_code}"

    return result_




def get_top():
    url = "https://toonily.com/webtoons/?m_orderby=trending"
    scrapped_page = scraper_splash(url=url)
    response = scrapped_page.find('div', class_="page-content-listing item-big_thumbnail")
    top_list = response.find_all('div', class_="col-6 col-sm-3 col-lg-2 badge-pos-2")
    items_list = []

# Find all the relevant divs

    for item in top_list:
    # Extract the title
        title_tag = item.find('h3', class_='h5')
        title = title_tag.get_text(strip=True) if title_tag else 'No Title'

        # Extract the image URL
        img_tag = item.find('img', class_='img-responsive')
        img_url = img_tag['src'] if img_tag else 'No Image URL'

        # Extract the rating
        rating_tag = item.find('span', property='ratingValue')
        rating = rating_tag.get_text(strip=True) if rating_tag else 'No Rating'

        # Extract viewers
        viewers_div = item.find('div', class_='manga-rate-view-comment')
        if viewers_div:
            viewers_tag = viewers_div.find('div', class_='item')
            viewers = viewers_tag.get_text(strip=True) if viewers_tag else 'No Viewers'
        else:
            viewers = 'No Viewers'

        # Extract the list of latest chapters
        chapters = []
        chapters_div = item.find('div', class_='list-chapter')
        if chapters_div:
            chapter_items = chapters_div.find_all('div', class_='chapter-item')
            for chapter in chapter_items:
                chapter_title_tag = chapter.find('span', class_='chapter')
                chapter_title = chapter_title_tag.get_text(strip=True) if chapter_title_tag else 'No Chapter Title'
                chapters.append(chapter_title)
        else:
            chapters = []

        # Create a dictionary for the item
        item_dict = {
            'title': title,
            'img_url': img_url,
            'rating': rating,
            'viewers': viewers,
            'chapters': chapters
        }

        # Append the dictionary to the list
        items_list.append(item_dict)
    return items_list



get_top()