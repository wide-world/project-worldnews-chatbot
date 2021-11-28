import requests
from bs4 import BeautifulSoup
import os

def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_image_link(link, image_link, url):
    news_url = link
    soup = create_soup(news_url)
    new_image_link = soup.find("div", attrs={"class" : "responsive-image"}).find("img")["src"]
    image_link.append(url + new_image_link+'\n')

def scrape_content(link, article):
    soup = create_soup(link)
    tmp=[]
    try:
        news_content = soup.find("div", attrs={"class" : "wysiwyg wysiwyg--all-content css-1vsenwb"}).find_all("p")       
        
        for news in news_content:
            text = news.get_text().strip()
            tmp.append(text)
        tmp.append('\n')
        article.append(tmp)
    except:
        tmp.append("Failed to get content!\n")
        article.append(tmp);

def scrape_news():
    url = "https://www.aljazeera.com"
    res = requests.get(url, headers={'User-Agent' : 'Mozilla/5.0'})
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    soup = create_soup(url)
    news_list = soup.find("div", attrs={"id" : "most-read-container"}).find_all("h3")

    news_link=[]
    image_link=[]
    article=[]
    for news in news_list:
        title = news.find("span").get_text().strip()
        link = url + news.find("a")["href"]
        scrape_image_link(link, image_link, url)
        scrape_content(link, article)
        news_link.append(title + '\n' + link + '\n')

    if os.path.exists('alj.txt'):
        os.remove('alj.txt')
    if os.path.exists('contents/scrapping/aljcontent.txt'):
        os.remove('contents/scrapping/aljcontent.txt')
    
    alj_fp = open('alj.txt', 'w', encoding='utf-8')
    for i in range(5):
        alj_fp.writelines(news_link[i])
    for i in range(5):
        alj_fp.writelines(image_link[i])

    aljcontent_fp = open('contents/scrapping/aljcontent.txt', 'w', encoding='utf-8')
    for i in range(5):
        aljcontent_fp.writelines(article[i])
                       
    alj_fp.close()
    aljcontent_fp.close()
    
if __name__ == "__main__":
    scrape_news()
