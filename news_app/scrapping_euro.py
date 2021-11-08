import requests
from bs4 import BeautifulSoup
import os
import sys

def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_news():
    if os.path.exists('euro.txt'):
        os.remove('euro.txt')

    print("EURO")
    url = "https://www.euronews.com/programs/world"
    res = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    soup = create_soup(url)
    news_list = soup.find_all("div", attrs={"class" : "c-most-viewed__article"})

    arr=[]
    for index, news in enumerate(news_list):
        title = news.find("a")["title"]
        link = url.replace('/programs/world', '') + news.find("a")["href"]
        arr.append(title + '\n' + link + '\n')
    
    euro_fp = open('euro.txt','w',encoding='utf-8')
    for i in range(len(arr)):
        euro_fp.writelines(arr[i])

if __name__ == "__main__":
    scrape_news()


