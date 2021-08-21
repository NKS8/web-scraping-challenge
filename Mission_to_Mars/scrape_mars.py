from splinter import Browser
from bs4 import BeautifulSoup
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd 

def scrape_info():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit mars site for title and news paragraph
    url = "https://redplanetscience.com"
    browser.visit(url)
    # gives time for website a little time to load 
    time.sleep(5)

    # Scrape page into Soup
    soup = BeautifulSoup(browser.html,'html.parser')

    # mars latest news and its title
    content_title = soup.find_all('div', class_ = 'content_title')[0].text
    news_p = soup.find_all('div', class_ = 'article_teaser_body')[0].text

    mars_data = {
        "content_title" : content_title,
        "news_p": news_p, 
        "featured_image_url": scrape_img()
                }
    # Quite the browser after scraping
    browser.quit()

    # Return results
    return mars_data 

def scrape_img():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit mars site for title and news paragraph
    url = "https://spaceimages-mars.com/"
    browser.visit(url)
    # gives time for website a little time to load 
    time.sleep(5)

    # Scrape page into Soup
    soup = BeautifulSoup(browser.html,'html.parser')
    f_image = soup.find('img', class_='headerimage fade-in')['src']
    featured_image_url = url + f_image
    return featured_image_url
