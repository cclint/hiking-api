from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path
import time

def test_page_titles_are_correct():
    svc = Service(binary_path)
    print(binary_path)
    browser = webdriver.Chrome(service=svc)

    browser.get('https://www.google.com/')

    search_bar = browser.find_element(By.NAME,"q")
    search_bar.send_keys("Poop Images")
    search_bar.submit()
    time.sleep(2)
    
    images_link = browser.find_element(By.LINK_TEXT, "Images")
    images_link.click
    time.sleep(10)


    browser.quit()

test_page_titles_are_correct()