#!/usr/bin/python3

from models.engine.db_storage import DBStorage
from models.quote import Quote
from models.category import Category

# Initialize the DBStorage engine
db_storage = DBStorage()
db_storage.reload()

# Create instances of models
category1 = Category(name="Category 1")
quote1 = Quote(text="Quote 1", author="Author 1", category=category1)
category2 = Category(name="Category 2")
quote2 = Quote(text="Quote 2", author="Author 2", category=category2)

# Add instances to the session
db_storage.new(category1)
db_storage.new(quote1)
db_storage.new(category2)
db_storage.new(quote2)

# Commit changes
db_storage.save()

# Query the database to verify
all_quotes = db_storage.all(Quote)
all_categories = db_storage.all(Category)

# Print the results to verify
print("Quotes:")
for quote in all_quotes.values():
    print(quote.text, quote.author, quote.category.name)

print("Categories:")
for category in all_categories.values():
    print(category.name)
