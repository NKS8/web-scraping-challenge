from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")

# Route to render index.html template using data from Mongo
@app.route("/")
def index():

    # Find one record of data from the mongo database
    data = mongo.db.mars_collection.find_one()

    # Return template and data
    return render_template("index.html",m_data=data)
# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function

    mars_data = scrape_mars.scrape_info()
    
    mongo.db.mars_collection.update({}, mars_data, upsert=True)
    # Redirect back to home page
    # 302 is status code is like slang 
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)