# web-scraping-challenge
## 12

It is a web application that scraped various websites for data related to the Mission to Mars and displayd the information in a single HTML page. 

![Screenshot 2021-08-25 014200](https://user-images.githubusercontent.com/67448948/130733009-923cc8c4-9e00-4baa-851f-5ba2eecbd85d.png)

Initial scraping used Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter and various objects were scraped such as titles, paragraph text, images, table, titles, and lsit of images and titles by their associated tags. 

1. scrape_mars.py scrapes information for the web application. 
    * created connection
    * visited site usring browser.visit()
    * created sop objects
    * scvraped information by using tags and attributes
    * created scraping functions for each sited scraping and returned colllected data
    * added collected data into dictionary in scrape_info() function. 
2. Python flask app was built.
    * flask app is created by Flask() obj
    * created mongo connection by using PyMongo through local host with database
    * set up scrape route with scrape function. 
    * collected data from scrape_info function in scrape_mars file
    * updated scraped data intp mongo db by using mongo CRUD
    * set up index route and rendered data into html file by accessing data in mongo collection 
3. Items/objects styled int he tags accordingly.
    * Titles created
    * Buttons created
    * featured image is rendered and table are wrapped in the same row
    * list of images and titles below are wrapped in row and containers.
   
