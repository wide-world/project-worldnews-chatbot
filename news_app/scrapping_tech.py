import requests
from bs4 import BeautifulSoup
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from pyvirtualdisplay import Display
import time

def scrape_links(url,title_arr,link_arr, image_arr):
    display = Display(visible=0, size=(1920, 1080))
    display.start()
    s = Service("/home/ubuntu/chromedriver")
    driver = webdriver.Chrome(service=s)
    driver.get(url)
    t = webdriver.Chrome(service=s)

    #1
    try:
        link = driver.find_element(By.XPATH,'//*[@id="topos-component"]/div[3]/div[1]/div/div[1]/div/div[2]/div[1]/a').get_attribute('href')
        t.get(link)
        title = t.find_element(By.XPATH, '//*[@id="main-heading"]').text
        title_arr.append(title)
        link_arr.append(link)
        try:
            image = driver.find_element(By.XPATH,'//*[@id="topos-component"]/div[3]/div[1]/div/div[1]/div/div[1]/div/div/img').get_attribute('src')
            image_arr.append(image)
        except:
            image_arr.append('https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20140619_95%2Fsungyoung2c_1403165753672QSa8b_JPEG%2F%25B3%25D7%25C0%25CC%25B9%25F6_%25B0%25CB%25BB%25F6%25B4%25A9%25B6%25F4.jpg&type=sc960_832')
    except:
        title_arr.append("Home Page")
        link_arr.append(url)
        image_arr.append('https://i.pinimg.com/736x/0a/3e/3f/0a3e3f002bfd508b0a8cb0b15e3ae284.jpg')

    #2
    try:
        link = driver.find_element(By.XPATH,'//*[@id="topos-component"]/div[3]/div[2]/div[1]/div/div/div/div[3]/div/div[1]/div/div[2]/div[1]/a').get_attribute('href')
        t.get(link)
        title = t.find_element(By.XPATH, '//*[@id="main-heading"]').text
        title_arr.append(title)
        link_arr.append(link)
        try:
            image = driver.find_element(By.XPATH,'//*[@id="topos-component"]/div[3]/div[2]/div[1]/div/div/div/div[3]/div/div[1]/div/div[1]/div/div/img').get_attribute('src')
            image_arr.append(image)
        except:
            image_arr.append('https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20140619_95%2Fsungyoung2c_1403165753672QSa8b_JPEG%2F%25B3%25D7%25C0%25CC%25B9%25F6_%25B0%25CB%25BB%25F6%25B4%25A9%25B6%25F4.jpg&type=sc960_832')
    except:
        title_arr.append("Home Page")
        link_arr.append(url)
        image_arr.append('https://i.pinimg.com/736x/0a/3e/3f/0a3e3f002bfd508b0a8cb0b15e3ae284.jpg')

    #3
    try:
        link = driver.find_element(By.XPATH,'//*[@id="topos-component"]/div[3]/div[2]/div[1]/div/div/div/div[3]/div/div[2]/div/div[2]/div[1]/a').get_attribute('href')
        t.get(link)
        title = t.find_element(By.XPATH, '//*[@id="main-heading"]').text
        title_arr.append(title)
        link_arr.append(link)
        try:
            image = driver.find_element(By.XPATH,'//*[@id="topos-component"]/div[3]/div[2]/div[1]/div/div/div/div[3]/div/div[2]/div/div[1]/div/div/img').get_attribute('src')
            image_arr.append(image)
        except:
            image_arr.append('https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20140619_95%2Fsungyoung2c_1403165753672QSa8b_JPEG%2F%25B3%25D7%25C0%25CC%25B9%25F6_%25B0%25CB%25BB%25F6%25B4%25A9%25B6%25F4.jpg&type=sc960_832')
    except:
        title_arr.append("Home Page")
        link_arr.append(url)
        image_arr.append('https://i.pinimg.com/736x/0a/3e/3f/0a3e3f002bfd508b0a8cb0b15e3ae284.jpg')

    #4
    try:
        link = driver.find_element(By.XPATH,'//*[@id="topos-component"]/div[3]/div[2]/div[1]/div/div/div/div[3]/div/div[3]/div/div[2]/div[1]/a').get_attribute('href')
        t.get(link)
        title = t.find_element(By.XPATH, '//*[@id="main-heading"]').text
        title_arr.append(title)
        link_arr.append(link)
        try:
            image = driver.find_element(By.XPATH,'//*[@id="topos-component"]/div[3]/div[2]/div[1]/div/div/div/div[3]/div/div[3]/div/div[1]/div/div/img').get_attribute('src')
            image_arr.append(image)
        except:
            image_arr.append('https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20140619_95%2Fsungyoung2c_1403165753672QSa8b_JPEG%2F%25B3%25D7%25C0%25CC%25B9%25F6_%25B0%25CB%25BB%25F6%25B4%25A9%25B6%25F4.jpg&type=sc960_832')
    except:
        title_arr.append("Home Page")
        link_arr.append(url)
        image_arr.append('https://i.pinimg.com/736x/0a/3e/3f/0a3e3f002bfd508b0a8cb0b15e3ae284.jpg')

    t.quit()
    driver.quit()
    display.stop()

def scrape_news():
    url = "https://www.bbc.com/news/technology"
    title_arr=[]
    link_arr=[]
    image_arr=[]

    scrape_links(url,title_arr,link_arr,image_arr)
    
    if os.path.exists('tech.txt'):
        os.remove('tech.txt')

    tech_fp = open('tech.txt', 'w', encoding='utf-8')
    for i in range(len(title_arr)):
        tech_fp.writelines(title_arr[i] + '\n')
        tech_fp.writelines(link_arr[i] + '\n')
        tech_fp.writelines(image_arr[i] + '\n')

    tech_fp.close()

if __name__ == "__main__":
    scrape_news()
