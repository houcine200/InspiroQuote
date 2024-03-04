#!/usr/bin/python3

from flask import Flask, render_template, redirect, url_for, request, jsonify, g, make_response
import requests
from models.category import Category
from models.quote import Quote
from models.engine.db_storage import DBStorage, storage
from models.user import User

app = Flask(__name__)
db_storage = DBStorage()
db_storage.reload()

def load_logged_in_user():
    g.user = None
    if 'user_email' in request.cookies:
        user_email = request.cookies.get('user_email')
        response = requests.get(API_URL)
        if response.status_code == 200:
            users = response.json()
            for user in users:
                if user['email'] == user_email:
                    g.user = user
                    break

@app.route('/', methods=['GET'], strict_slashes=False)
@app.route('/home', methods=['GET'], strict_slashes=False)
def home():
    load_logged_in_user()  # Load current user
    user = g.user if hasattr(g, 'user') else None
    return render_template("home.html", user=user)

@app.route('/categories', methods=['GET'], strict_slashes=False)
def categories():
    load_logged_in_user()  # Load current user
    user = g.user if hasattr(g, 'user') else None
    return render_template('categories.html', user=user)

@app.route('/authors', methods=['GET'], strict_slashes=False)
def authors():
    load_logged_in_user()  # Load current user
    user = g.user if hasattr(g, 'user') else None
    return render_template('authors.html', user=user)

@app.route('/quote_of_the_day', methods=['GET'], strict_slashes=False)
def quote_of_the_day():
    load_logged_in_user()  # Load current user
    user = g.user if hasattr(g, 'user') else None
    return render_template('quote_of_the_day.html', user=user)

@app.route('/about', methods=['GET'], strict_slashes=False)
def about():
    load_logged_in_user()  # Load current user
    user = g.user if hasattr(g, 'user') else None
    return render_template('about.html', user=user)

@app.route('/register', methods=['GET'], strict_slashes=False)
def register():
    return render_template('registration.html')

@app.route('/index', methods=['GET'], strict_slashes=False)
def index():
    return render_template('index.html')

@app.route('/users', methods=['GET'], strict_slashes=False)
def users():
    return render_template('users.html')

API_URL = 'http://localhost:5001/api/v1/users'

def load_logged_in_user():
    g.user = None
    if 'user_email' in request.cookies:
        user_email = request.cookies.get('user_email')
        response = requests.get(API_URL)
        if response.status_code == 200:
            users = response.json()
            for user in users:
                if user['email'] == user_email:
                    g.user = user
                    break

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        
        all_users = storage.all(User)
        
        for user in all_users.values():
            if user.email == email and user.password == password:
                response = make_response(redirect(url_for("profile", email=email)))
                response.set_cookie('user_email', email)
                return response
        
        return render_template("login.html", error="Invalid email or password.")
    
    else:
        return render_template("login.html")

@app.route("/profile")
def profile():
    user_email = request.cookies.get('user_email')
    if not user_email:
        return jsonify({'error': 'User not logged in.'}), 401  # Unauthorized

    response = requests.get(API_URL)
    if response.status_code == 200:
        users = response.json()
        for user in users:
            if user['email'] == user_email:
                return render_template("profile.html", user=user)
        return jsonify({'error': 'User not found.'}), 404  # Not Found
    else:
        return jsonify({'error': 'An error occurred. Please try again later.'}), 500  # Internal Server Error

@app.route("/logout")
def logout():
    # Clear the user's cookie
    response = make_response(redirect(url_for("home")))
    response.set_cookie('user_email', '', expires=0)
    return response


@app.teardown_appcontext
def teardown_db(exception):
    """Close database connection."""
    db_storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
