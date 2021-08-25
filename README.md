# web-scraping-challenge
#12

A Web application that scraped various websites for data related to the Mission to Mars and displayd the information in a single HTML page. 

Initial scraping used Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter and various objects were scraped such as titles, paragraph text, images, table, titles, and lsit of images and titles by their associated tags. 

1. scrape_mars.py is scraped information for the web application. 
    1.a created connection
    1.b visited site usring browser.visit()
    1.c created sop object
    1.d scvraped information by using tags and attributes
    1.e created scraping functions for each sited scraping and returned colllected data
    1.f added collected data into dictionary in scrape_info() function