import requests
from bs4 import BeautifulSoup
import os
import sys
from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


def scrape_image_link(url, image_arr):
    display = Display(visible=0, size=(1920, 1080))
    display.start()
    path = '/home/ubuntu/chromedriver'
    s = Service(path)
    driver = webdriver.Chrome(service=s)
    driver.implicitly_wait(10)
    driver.get(url)

    try:
        driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="p-news__videoPlayer"]/div/div/div/iframe'))
        image = driver.find_element(By.XPATH, '//*[@id="nPlayerContainerAltContentVideoContentPosterFrame"]').get_attribute('style')
        tmp = image[23:-3]
        driver.switch_to.default_content()
        image_arr.append('https://www3.nhk.or.jp' + tmp)
    except:
        try:
            image =driver.find_element(By.XPATH,'//*[@id="p-article"]/div[2]/div/img').get_attribute('src')
            image_arr.append(image)
        except:
            image_arr.append('https://i.pinimg.com/736x/0a/3e/3f/0a3e3f002bfd508b0a8cb0b15e3ae284.jpg')
    finally:
        driver.quit()
        display.stop()

def scrape_link(url, link_arr, title_arr):
    display = Display(visible=0, size=(1920, 1080))
    display.start()
    path = '/home/ubuntu/chromedriver'
    s=Service(path)

    driver = webdriver.Chrome(service=s)
    driver.get(url)
    depth_1 = driver.find_element(By.CLASS_NAME, "c-ranking")
    depth_2 = depth_1.find_elements(By.TAG_NAME, "a")
    for news in depth_2:
        link =  news.get_attribute('href')
        title = news.text
        link_arr.append(link)
        title_arr.append(title)

    driver.quit()
    display.stop()

def scrape_text(url,article):
    res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    depth_1 = soup.find("div", attrs={"class": "p-article__body"}).find_all("p")
    tmp=[]
    for news in depth_1:
        text = news.get_text().strip()
        text = ' '.join(text.split('\n'))
        tmp.append(text)
    tmp.append('\n')
    article.append(tmp)

def scrape_news():
    title_arr=[]
    link_arr=[]
    image_arr=[]
    article=[]
    link = "https://www3.nhk.or.jp/nhkworld/en/news/"

    scrape_link(link, link_arr, title_arr)

    for link in link_arr:
        scrape_image_link(link, image_arr)

    for link in link_arr:
        scrape_text(link,article)

    if os.path.exists('nhk.txt'):
        os.remove('nhk.txt')

    nhk_fp = open('nhk.txt','w',encoding='utf-8')
    for i in range(len(title_arr)):
        nhk_fp.writelines(title_arr[i] + '\n')
        nhk_fp.writelines(link_arr[i] + '\n')
    for i in range(len(image_arr)):
        nhk_fp.writelines(image_arr[i] + '\n')

    if os.path.exists('contents/scrapping/nhkcontent.txt'):
        os.remove('contents/scrapping/nhkcontent.txt')
    text_fp = open('contents/scrapping/nhkcontent.txt', 'w', encoding='utf-8')
    for i in range(len(article)):
        text_fp.writelines(article[i])

    text_fp.close()
    nhk_fp.close()

if __name__ == "__main__":
    scrape_news()
