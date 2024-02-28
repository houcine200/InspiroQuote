#!/usr/bin/python3

from flask import Flask, render_template
from models.category import Category
from models.quote import Quote
from models.engine.db_storage import DBStorage

app = Flask(__name__)
db_storage = DBStorage()
db_storage.reload()


@app.route('/', methods=['GET'], strict_slashes=False)
@app.route('/home', methods=['GET'], strict_slashes=False)
def home():
    return render_template('home.html')

@app.route('/categories', methods=['GET'], strict_slashes=False)
def categories():
    return render_template('categories.html')

@app.route('/authors', methods=['GET'], strict_slashes=False)
def authors():
    return render_template('authors.html')

@app.route('/quote_of_the_day', methods=['GET'], strict_slashes=False)
def quote_of_the_day():
    return render_template('quote_of_the_day.html')

@app.route('/about', methods=['GET'], strict_slashes=False)
def about():
    return render_template('about.html')

@app.teardown_appcontext
def teardown_db(exception):
    """Close database connection."""
    db_storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
