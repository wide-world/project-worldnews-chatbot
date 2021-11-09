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

display = Display(visible=0, size=(1920, 1080))
display.start()

path = '/home/ubuntu/chromedriver'
driver = webdriver.Chrome(path)

#def scrape_all(url, link_arr, title_arr, image_link):
def scrape_all(url, link_arr, title_arr):
    driver.get(url)

    #1
    depth_1 = driver.find_element(By.CLASS_NAME, "cn-list-hierarchical-xs")
    depth_2 = depth_1.find_element(By.CLASS_NAME, "banner-text")
    depth_2_2 = depth_1.find_element(By.TAG_NAME,'a')
    #depth_3 = depth_2_2.find_element(By.XPATH, '//*[@id="intl_homepage1-zone-1"]/div[2]/div/div[1]/ul/li[1]/article/div/div[1]/a/img')
    #img = depth_3.get_attribute('src')

    link = depth_2_2.get_attribute('href')
    title = depth_2.text
    link_arr.append(link)
    title_arr.append(title)
    #image_link.append(img)

    #2
    depth_1 = driver.find_element(By.XPATH, '//*[@id="intl_homepage1-zone-1"]/div[2]/div/div[2]/ul/li[1]/article/div/div[2]/h3')
    depth_2 = depth_1.find_element(By.TAG_NAME, "a")
    depth_3 = depth_2.find_element(By.XPATH,'//*[@id="intl_homepage1-zone-1"]/div[2]/div/div[2]/ul/li[1]/article/div/div[2]/h3/a/span[2]')

    #before_img = driver.find_element(By.XPATH,'//*[@id="intl_homepage1-zone-1"]/div[2]/div/div[2]/ul/li[1]/article/div/div[1]/a/img')
    #img = before_img.get_attribute('src')
    #image_link.append(img)

    title = depth_3.text
    title_arr.append(title)

    link = depth_2.get_attribute('href')
    link_arr.append(link)

    #3
    depth_1 = driver.find_element(By.XPATH, '//*[@id="intl_homepage1-zone-1"]/div[2]/div/div[2]/ul/li[2]/article/div/div[2]/h3/a/span[2]')
    title = depth_1.text
    title_arr.append(title)

    before_link = driver.find_element(By.XPATH, '//*[@id="intl_homepage1-zone-1"]/div[2]/div/div[2]/ul/li[2]/article/div/div[2]/h3/a')
    link = before_link.get_attribute('href')
    link_arr.append(link)

    #before_img = driver.find_element(By.XPATH, '//*[@id="intl_homepage1-zone-1"]/div[2]/div/div[2]/ul/li[2]/article/div/div[1]/a/img')
    #img = before_img.get_attribute('data-src-small')
    #image_link.append(img)

    #4
    before_title = driver.find_element(By.XPATH, '//*[@id="intl_homepage1-zone-1"]/div[2]/div/div[3]/ul/li[1]/article/div/div[2]/h3/a/span[2]')
    title = before_title.text
    title_arr.append(title)

    before_link = driver.find_element(By.XPATH, '//*[@id="intl_homepage1-zone-1"]/div[2]/div/div[3]/ul/li[1]/article/div/div[2]/h3/a')
    link = before_link.get_attribute('href')
    link_arr.append(link)

    #before_img = driver.find_element(By.XPATH, '//*[@id="intl_homepage1-zone-1"]/div[2]/div/div[3]/ul/li[1]/article/div/div[1]/a/img')
    #img = before_img.get_attribute('src')
    #image_link.append(img)

    driver.close()

def scrape_news():
    title_arr=[]
    link_arr=[]
    image_link=[]

    link = "https://edition.cnn.com/"
    #scrape_all(link, link_arr, title_arr, image_link)
    scrape_all(link, link_arr, title_arr)

    if os.path.exists('cnn.txt'):
        os.remove('cnn.txt')

    cnn_fp = open('cnn.txt', 'w', encoding='utf-8')
    for i in range(len(title_arr)):
        cnn_fp.writelines(title_arr[i] + '\n')
        cnn_fp.writelines(link_arr + '\n')
    #for i in range(len(image_link)):
    #    cnn_fp.writelines(image_link[i])

    print("CNN")
        
if __name__ == "__main__":
    scrape_news()
