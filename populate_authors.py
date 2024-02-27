#!/usr/bin/python3

from models.engine.db_storage import DBStorage
from models.citation import Citation
from models.author import Author

# Initialize the DBStorage engine
db_storage = DBStorage()
db_storage.reload()

# Create instances of models
author1 = Author(name="Author 1")
citation1 = Citation(text="Citation 1", author=author1)
author2 = Author(name="Author 2")
citation2 = Citation(text="Citation 2", author=author2)

# Add instances to the session
db_storage.new(author1)
db_storage.new(citation1)
db_storage.new(author2)
db_storage.new(citation2)

# Commit changes
db_storage.save()

# Query the database to verify
all_citations = db_storage.all(Citation)
all_authors = db_storage.all(Author)

# Print the results to verify
print("Citations:")
for citation in all_citations.values():
    print(citation.text, citation.author.name)

print("Authors:")
for author in all_authors.values():
    print(author.name)
