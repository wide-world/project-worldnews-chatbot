#from django.test import TestCase
import requests
from bs4 import BeautifulSoup


def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup


def scrape_news():
    print("[news]")
    url = "https://www.bbc.com/news"
    res = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    soup = create_soup(url)
    news_list = soup.find("ol", attrs={"class" : "gel-layout__item gs-u-float-left@l"}).find_all("li")
    for index, news in enumerate(news_list):
        title = news.find("a").get_text().strip()
        link = url.replace('/news', '')+news.find("a")["href"]
        print("{}. {}".format(index+1, title))
        print(" (링크) : {})".format(link))

    print()


if __name__ == "__main__":
    scrape_news()
