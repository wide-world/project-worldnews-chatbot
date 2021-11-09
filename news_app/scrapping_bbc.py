from bs4 import BeautifulSoup
import requests
import os
import sys

def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup


def scrape_image_link(link, image_link):
    url = link
    #res = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
    #res.raise_for_status()
    #soup = BeautifulSoup(res.text, "lxml")
    soup = create_soup(url)
    new_image_link = soup.find("div", attrs={"class" : "ssrcss-ab5fd8-StyledFigureContainer e34k3c21"}).find("img")["src"]
    image_link.append(new_image_link)


def scrape_news():
    url = "https://www.bbc.com/news"
    res = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    soup = create_soup(url)
    news_list = soup.find("ol", attrs={"class" : "gel-layout__item gs-u-float-left@l"}).find_all("li")
    
    arr=[]
    image_link=[]
    for index, news in enumerate(news_list):
        title = news.find("a").get_text().strip()
        link = url.replace('/news', '')+news.find("a")["href"]
        #scrape_image_link(link, image_link)
        arr.append(title+'\n'+link+'\n')
        #print("{}. {}".format(index+1, title))
        #print(" (링크) : {})".format(link))

    if os.path.exists('bbc.txt'):
        os.remove('bbc.txt')

    bbc_fp = open('bbc.txt','w',encoding='utf-8')
    for i in range(len(arr)):
        bbc_fp.writelines(arr[i])

    for i in range(len(image_link)):
        bbc_fp.writelinkes(image_link(i))
    
    bbc_fp.close()

if __name__ == "__main__":
    scrape_news()


