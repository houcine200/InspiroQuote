#!/usr/bin/python3

from models.engine.db_storage import DBStorage
from models.user import User
from models.review import Review

# Initialize the DBStorage engine
db_storage = DBStorage()
db_storage.reload()

# Create instances of models for users with reviews
users_with_reviews = [
    User(email="user1@example.com", password="password", first_name="John", last_name="Doe", reviews=[
        Review(text="Great website!"),
        Review(text="Excellent experience"),
    ]),
    User(email="user2@example.com", password="password", first_name="Jane", last_name="Smith", reviews=[
        Review(text="Awesome quotes!"),
        Review(text="Very inspiring"),
    ]),
    # Add more users with their reviews as needed
]

# Add instances to the session
for user in users_with_reviews:
    db_storage.new(user)
    for review in user.reviews:
        db_storage.new(review)

# Commit changes
db_storage.save()
