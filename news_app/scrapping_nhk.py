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

display = Display(visible=0, size=(1920, 1080))
display.start()

path = '/home/ubuntu/chromedriver' 
driver = webdriver.Chrome(path)

def scrape_image_link(url, link_arr, title_arr):
    driver.get(url)
    depth_1 = driver.find_element(By.CLASS_NAME, "c-ranking")
    depth_2 = depth_1.find_elements(By.TAG_NAME, "a")
    for news in depth_2:
        link =  news.get_attribute('href')
        title = news.text
        link_arr.append(link)
        title_arr.append(title)

    driver.close()

def scrape_news():
    title_arr=[]
    link_arr=[]
    link = "https://www3.nhk.or.jp/nhkworld/en/news/"
    scrape_image_link(link, link_arr, title_arr)

    if os.path.exists('nhk.txt'):
        os.remove('nhk.txt')
    
    nhk_fp = open('nhk.txt','w',encoding='utf-8')
    for i in range(len(title_arr)):
        nhk_fp.writelines(title_arr[i] + '\n')
        nhk_fp.writelines(link_arr[i] + '\n')
    
    print("NHK")

if __name__ == "__main__":
    scrape_news()
