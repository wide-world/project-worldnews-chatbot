import requests
from bs4 import BeautifulSoup
import os

def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_image_link(link, image_link):
    news_url = link
    soup = create_soup(news_url)
    new_image_link = soup.find("div", attrs={"class" : "c-video-player__container"}).find("img")["src"]
    image_link.append(new_image_link+'\n')

def scrape_content(link, article):
    soup = create_soup(link)
    news_content = soup.find("div", attrs={"class" : "js-responsive-iframes-container"}).find_all("p")
    tmp=[]
    for news in enumerate(news_content):
        text = news.get_text().strip()
        tmp.append(text)
    tmp.append('\n')
    article.append(tmp)

def scrape_news():
    url = "https://www.euronews.com/programs/world"
    res = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    soup = create_soup(url)
    news_list = soup.find_all("div", attrs={"class" : "c-most-viewed__article"})

    news_link=[]
    image_link=[]
    article=[]
    for news in enumerate(news_list):
        title = news.find("a")["title"]
        link = url.replace('/programs/world', '') + news.find("a")["href"]
        scrape_image_link(link, image_link)
        scrape_content(link, article)
        news_link.append(title + '\n' + link + '\n')

    if os.path.exists('euro.txt'):
        os.remove('euro.txt')
    if os.path.exists('contents/scrapping/eurocontent.txt'):
        os.remove('contents/scrapping/eurocontent.txt')

    euro_fp = open('euro.txt','w',encoding='utf-8')
    for i in range(len(news_link)):
        euro_fp.writelines(news_link[i])
    for i in range(len(image_link)):
        euro_fp.writelines(image_link[i])
    
    eurocontent_fp = open('contents/scrapping/eurocontent.txt', 'w', encoding='utf-8')
    for i in range(len(article)):
        eurocontent_fp.writelines(article[i])
    
    eurocontent_fp.close()
    euro_fp.close()

if __name__ == "__main__":
    scrape_news()
