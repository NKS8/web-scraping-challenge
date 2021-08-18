# -----------------------------------------
# importing all dependencies/library/classes
# ------------------------------------------


import numpy as np
import pandas as pd
import datetime as dt
from flask_pymongo import PyMongo

from flask import Flask, jsonify, render_template


app = Flask(__name__) 

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"

@app.route("/")
def welcome():
    return render_template('index.html')
    

if __name__ == "__main__":
    app.run(debug=True)
