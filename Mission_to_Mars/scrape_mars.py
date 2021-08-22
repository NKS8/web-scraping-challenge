from splinter import Browser
from bs4 import BeautifulSoup
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd 


def scrape_info():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit mars site for title and news paragraph
    url = "https://redplanetscience.com"
    browser.visit(url)
    # gives time for website a little time to load 
    time.sleep(2)

    # Scrape page into Soup
    soup = BeautifulSoup(browser.html,'html.parser')

    # mars latest news and its title
    content_title = soup.find_all('div', class_ = 'content_title')[0].text
    news_p = soup.find_all('div', class_ = 'article_teaser_body')[0].text

    mars_data = {
        "content_title" : content_title,
        "news_p": news_p, 
        "featured_image_url": scrape_img(browser),
        "mars_facts": scrape_table(browser),
        "hemisphere_image_urls" : scrape_hemisphere(browser)
                }
    # Quite the browser after scraping
    browser.quit()

    # Return results
    return mars_data 

def scrape_img(browser):
    # Visit mars site for title and news paragraph
    url = "https://spaceimages-mars.com/"
    browser.visit(url)
    # gives time for website a little time to load 
    time.sleep(2)

    # Scrape page into Soup
    soup = BeautifulSoup(browser.html,'html.parser')
    f_image = soup.find('img', class_='headerimage fade-in')['src']
    featured_image_url = url + f_image
    return featured_image_url

def scrape_table(browser): 

    # Visit mars site for title and news paragraph
    url = "https://galaxyfacts-mars.com/"

    # gives time for website a little time to load 
    # since it is table, not using soupr rather using pandas
   
    tables = pd.read_html(url)
    facts_df = tables[0]
    facts_df.columns = ["Mars-Earth Comparison", "Mars","Earth"]
    facts_df.set_index("Mars-Earth Comparison", inplace = True)
    df = facts_df.iloc[1:]
    mars_facts = df.to_html()
    print(mars_facts)

    return mars_facts


def scrape_hemisphere(browser):
    hems_url = 'https://marshemispheres.com/'
    browser.visit(hems_url)
    time.sleep(2)
    # Scrape page into Soup
    soup = BeautifulSoup(browser.html,'html.parser')
    img_title = soup.find_all('img', class_ = 'thumb')

    for i in range(len(img_title)):
        h_title = img_title[i]['src']
        img_url = img_title[i]['alt']

        hemisphere_image_urls = {"title": h_title,
                             "img_url": img_url
                            }
    return hemisphere_image_urls



