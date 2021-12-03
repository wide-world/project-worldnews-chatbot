import requests
from bs4 import BeautifulSoup
import os
import sys
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pyvirtualdisplay import Display
import time


def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_text(url,article):
    res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    try:
        depth_1 = soup.find_all("div", attrs={"class": "zn-body__paragraph"})
        tmp=[]

        for news in depth_1:
            text=news.get_text().strip()
            tmp.append(text)
        
        if len(tmp) == 0:
            tmp.append('Failed to get content!')
        
        tmp.append('\n')
        article.append(tmp)
    except:
        tmp=[]
        tmp.append('Failed to get content!\n')
        article.append(tmp)

def scrape_links(url,title_arr,link_arr, image_arr):
    display = Display(visible=0, size=(1920, 1080))
    display.start()

    s = Service("/home/ubuntu/chromedriver")
    driver = webdriver.Chrome(service=s)
    driver.get(url)

    #1
    try:
        link = driver.find_element(By.XPATH,'//*[@id="intl_homepage1-zone-1"]/div[2]/div/div[1]/ul/li[1]/article/div/div[2]/h3/a').get_attribute('href')
        # title = driver.find_element(By.XPATH,'//*[@id="intl_homepage-injection-zone-1"]/div[2]/div/div/div/ul/li[4]/article/div/div/h3/a/span[1]').text
        link_arr.append(link)
        title = driver.find_element(By.XPATH, '//*[@id="intl_homepage1-zone-1"]/div[2]/div/div[1]/ul/li[1]/article/div/div[2]/h3/a/span[2]').text
        title_arr.append(title)
        try:
            image = driver.find_element(By.XPATH,'//*[@id="intl_homepage1-zone-1"]/div[2]/div/div[1]/ul/li[1]/article/div/div[1]/a/img').get_attribute('data-src-xsmall')
            image_arr.append('https:' + image)
        except:
            image_arr.append('https://i.pinimg.com/736x/0a/3e/3f/0a3e3f002bfd508b0a8cb0b15e3ae284.jpg')
    except:
        title_arr.append("Home Page")
        link_arr.append(url)
        image_arr.append('https://i.pinimg.com/736x/0a/3e/3f/0a3e3f002bfd508b0a8cb0b15e3ae284.jpg')


    #2
    try:
        link = driver.find_element(By.XPATH,'//*[@id="intl_homepage1-zone-1"]/div[2]/div/div[2]/ul/li[1]/article/div/div[2]/h3/a').get_attribute('href')
        link_arr.append(link)
        title = driver.find_element(By.XPATH, '//*[@id="intl_homepage1-zone-1"]/div[2]/div/div[2]/ul/li[1]/article/div/div[2]/h3/a/span[2]').text
        title_arr.append(title)
        try:
            image = driver.find_element(By.XPATH,'//*[@id="intl_homepage1-zone-1"]/div[2]/div/div[2]/ul/li[1]/article/div/div[1]/a/img').get_attribute('data-src-xsmall')
            image_arr.append('https:' + image)
        except:
            image_arr.append('https://i.pinimg.com/736x/0a/3e/3f/0a3e3f002bfd508b0a8cb0b15e3ae284.jpg')
    except:
        title_arr.append("Home Page")
        link_arr.append(url)
        image_arr.append('https://i.pinimg.com/736x/0a/3e/3f/0a3e3f002bfd508b0a8cb0b15e3ae284.jpg')

    #3
    try:
        link = driver.find_element(By.XPATH,'//*[@id="intl_homepage1-zone-1"]/div[2]/div/div[2]/ul/li[2]/article/div/div[2]/h3/a').get_attribute('href')
        link_arr.append(link)
        title = driver.find_element(By.XPATH, '//*[@id="intl_homepage1-zone-1"]/div[2]/div/div[2]/ul/li[2]/article/div/div[2]/h3/a/span[2]').text
        title_arr.append(title)
        try:
            image = driver.find_element(By.XPATH,'//*[@id="intl_homepage1-zone-1"]/div[2]/div/div[2]/ul/li[2]/article/div/div[1]/a/img').get_attribute('data-src-xsmall')
            image_arr.append('https:' + image)
        except:
            image_arr.append('https://i.pinimg.com/736x/0a/3e/3f/0a3e3f002bfd508b0a8cb0b15e3ae284.jpg')
    except:
        title_arr.append("Home Page")
        link_arr.append(url)
        image_arr.append('https://i.pinimg.com/736x/0a/3e/3f/0a3e3f002bfd508b0a8cb0b15e3ae284.jpg')

    #4
    try:
        link = driver.find_element(By.XPATH,'//*[@id="intl_homepage1-zone-1"]/div[2]/div/div[3]/ul/li[1]/article/div/div[2]/h3/a').get_attribute('href')
        link_arr.append(link)
        title = driver.find_element(By.XPATH, '//*[@id="intl_homepage1-zone-1"]/div[2]/div/div[3]/ul/li[1]/article/div/div[2]/h3/a/span[2]').text
        title_arr.append(title)
        try:
            image = driver.find_element(By.XPATH,'//*[@id="intl_homepage1-zone-1"]/div[2]/div/div[3]/ul/li[1]/article/div/div[1]/a/img').get_attribute('data-src-xsmall')
            image_arr.append('https:' + image)
        except:
            image_arr.append('https://i.pinimg.com/736x/0a/3e/3f/0a3e3f002bfd508b0a8cb0b15e3ae284.jpg')
    except:
        title_arr.append("Home Page")
        link_arr.append(url)
        image_arr.append('https://i.pinimg.com/736x/0a/3e/3f/0a3e3f002bfd508b0a8cb0b15e3ae284.jpg')

    driver.quit()
    display.stop()


def scrape_news():
    url = "https://edition.cnn.com/"
    title_arr=[]
    link_arr=[]
    image_arr=[]
    article=[]
    scrape_links(url,title_arr,link_arr,image_arr)

    if os.path.exists('cnn.txt'):
        os.remove('cnn.txt')

    cnn_fp = open('cnn.txt', 'w', encoding='utf-8')
    for i in range(len(title_arr)):
        cnn_fp.writelines(title_arr[i] + '\n')
        cnn_fp.writelines(link_arr[i] + '\n')
    for i in range(len(image_arr)):
        cnn_fp.writelines(image_arr[i] + '\n')

    for link in link_arr:
        scrape_text(link, article)

    if os.path.exists('contents/scrapping/cnncontent.txt'):
        os.remove('contents/scrapping/cnncontent.txt')
    text_fp = open('contents/scrapping/cnncontent.txt', 'w', encoding='utf-8')
    for i in range(len(article)):
        text_fp.writelines(article[i])

    text_fp.close()
    cnn_fp.close()


if __name__ == "__main__":
    scrape_news()



