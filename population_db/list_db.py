#!/usr/bin/python3

from models.engine.db_storage import DBStorage
from models.quote import Quote
from models.category import Category

# Initialize the DBStorage engine
db_storage = DBStorage()
db_storage.reload()

def list_all(table):
    """List all data of the specified table."""
    all_data = db_storage.all(table)
    table_name = table.__tablename__.capitalize()  # Get the table name

    print(f"All {table_name}s:")
    for data in all_data.values():
        print(f"[{table_name}] ({data.id}) {data.to_dict()}")

if __name__ == "__main__":
    list_all(Quote)
    list_all(Category)
