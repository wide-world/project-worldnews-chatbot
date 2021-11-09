import requests
from bs4 import BeautifulSoup
import os
import sys

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


def scrape_news():
    url = "https://www.aljazeera.com"
    res = requests.get(url, headers={'User-Agent' : 'Mozilla/5.0'})
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    soup = create_soup(url)
    news_list = soup.find("div", attrs={"id" : "most-read-container"}).find_all("h3")
    

    arr=[]
    image_link=[]
    for index, news in enumerate(news_list):
        title = news.find("span").get_text().strip()
        link = url + news.find("a")["href"]
        scrape_image_link(link, image_link, url)
        arr.append(title + '\n' + link + '\n')

    if os.path.exists('alj.txt'):
        os.remove('alj.txt')

    alj_fp = open('alj.txt', 'w', encoding='utf-8')
    for i in range(len(arr)):
        alj_fp.writelines(arr[i])
    for i in range(len(image_link)):
        alj_fp.writelines(image_link[i])
    
    alj_fp.close()

    print("ALJ")

if __name__ == "__main__":
    scrape_news()
