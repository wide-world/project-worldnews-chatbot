import requests
from bs4 import BeautifulSoup
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pyvirtualdisplay import Display
import time

display = Display(visible=0, size=(1920, 1080))
display.start()

path = '/home/ubuntu/chromedriver'
s=Service(path)
driver = webdriver.Chrome(service=s)

#driver = webdriver.Chrome(path)

def scrape_all(url, link_arr, title_arr, image_link):
    driver.get(url)

    #1
    try:
        link = driver.find_element(By.XPATH, '//*[@id="intl_homepage-injection-zone-1"]/div[2]/div/div/div/ul/li[3]/article/div/div/h3/a').get_attribute('href')
        title = driver.find_element(By.XPATH,'//*[@id="intl_homepage-injection-zone-1"]/div[2]/div/div/div/ul/li[3]/article/div/div/h3/a/span[2]').text
        link_arr.append(link)
        title_arr.append(title)
    except:
        image_link.append(1)

    #2
    try:
        link = driver.find_element(By.XPATH,'//*[@id="intl_homepage-injection-zone-1"]/div[2]/div/div/div/ul/li[4]/article/div/div/h3/a').get_attribute('href')
        title = driver.find_element(By.XPATH,'//*[@id="intl_homepage-injection-zone-1"]/div[2]/div/div/div/ul/li[4]/article/div/div/h3/a/span[1]').text
        link_arr.append(link)
        title_arr.append(title)
    except:
        image_link.append(1)

    #3
    try:
        link = driver.find_element(By.XPATH,'//*[@id="intl_homepage-injection-zone-1"]/div[2]/div/div/div/ul/li[5]/article/div/div/h3/a').get_attribute('href')
        title = driver.find_element(By.XPATH,'//*[@id="intl_homepage-injection-zone-1"]/div[2]/div/div/div/ul/li[5]/article/div/div/h3/a/span[1]').text
        link_arr.append(link)
        title_arr.append(title)
    except:
        image_link.append(1)

    #4
    try:
        link = driver.find_element(By.XPATH, '//*[@id="intl_homepage-injection-zone-1"]/div[2]/div/div/div/ul/li[6]/article/div/div/h3/a').get_attribute('href')
        title = driver.find_element(By.XPATH, '//*[@id="intl_homepage-injection-zone-1"]/div[2]/div/div/div/ul/li[6]/article/div/div/h3/a/span[1]').text
        link_arr.append(link)
        title_arr.append(title)
    except:
        image_link.append(1)

    #4
    try:
        link = driver.find_element(By.XPATH, '//*[@id="intl_homepage-injection-zone-1"]/div[2]/div/div/div/ul/li[7]/article/div/div/h3/a').get_attribute('href')
        title = driver.find_element(By.XPATH, '//*[@id="intl_homepage-injection-zone-1"]/div[2]/div/div/div/ul/li[7]/article/div/div/h3/a/span[1]').text
        link_arr.append(link)
        title_arr.append(title)
    except:
        image_link.append(1)
    
    driver.close()

def scrape_news():
    title_arr=[]
    link_arr=[]
    image_link=[]
    link = "https://edition.cnn.com/"
    scrape_all(link, link_arr, title_arr, image_link)
    # print(image_link)

    cnn_fp = open('cnn.txt', 'w', encoding='utf-8')
    for i in range(len(title_arr)):
        cnn_fp.writelines(title_arr[i] + '\n')
        cnn_fp.writelines(link_arr[i] + '\n')
    #for i in range(len(image_link)):
    #    cnn_fp.writelines(image_link[i])

if __name__ == "__main__":
    scrape_news()
