# Web-sSraping-Challenge
## 12


It is a web application that scraped from various websites and all data related to the Mission to Mars. Information required is displayd in a single HTML page. 

![Screenshot 2021-08-25 014200](https://user-images.githubusercontent.com/67448948/130733009-923cc8c4-9e00-4baa-851f-5ba2eecbd85d.png)

Initial scraping used Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter. Various objects were scraped such as Title, paragraphs, images, table, and list of images and its titles by their associated tags. 

1. scrape_mars.py scrapes all information needed for the web application. 
    * created connection
    * visited site using browser.visit()
    * created soup object
    * scraped information by using tags and attributes
    * created scraping functions for each site and returned colllected data relatively
    * added returned-data into dictionary in scrape_info() function. 
2. Python flask app was built.
    * flask app is created by Flask() obj
    * created mongo connection by using PyMongo through local host with database
    * set up scrape route with scrape function. 
    * collected data from scrape_info function in scrape_mars file
    * updated scraped data into mongo db by using mongo CRUD
    * set up index route and rendered data into html file by accessing data was added in mongo collection 
3. Items/objects styled in the tags accordingly.
    * Titles created
    * Button created
    * featured image is rendered and table are wrapped in the same row
    * list of images and titles below are wrapped in row and containers.
Web app is responsive and fucntion was created by BS. 
