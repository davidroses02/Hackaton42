import requests
from bs4 import BeautifulSoup

#url = 'https://www.amazon.es/Levis-Crewneck-Graphic-Camiseta-Heather/dp/B07LF5ZGVR/ref=sr_1_1_sspa?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=8O69ZOOZQVXA&keywords=camisetas&qid=1682195600&sprefix=camisetas%2Caps%2C167&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1&psc=1'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
def get_reviews(url):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')#traduce la pagina de html

    comments = soup.select('.review-text-content')#accede a los datos desde el css
    ratings = soup.select('.review-rating')

    comments_list = []
    for i in range(len(comments)):
        comments_list.append(comments[i].get_text(strip=True))# añade los comentarios a la lista comments_list
    return comments_list
    
