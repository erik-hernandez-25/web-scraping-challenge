from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
mongo = PyMongo(app)

# Route to index page to render Mongo data to template
@app.route("/")
def index():

    # Find one record of data from Mongo
    #mars_data = mongo.db.collection.find_one()
    
    # Activate jinja within the website index page
    #return render_template("index.html", data=mars_data)
    
    mars_data = mongo.db.collection.find_one()
    return render_template("index.html", mars_data=mars_data)



@app.route("/scrape")
def scraper():

    scrape_data = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, scrape_data, upsert=True)

    # Redirect back to home page
    return redirect("/", code= 302)

if __name__ == "__main__":
    app.run(debug=True)