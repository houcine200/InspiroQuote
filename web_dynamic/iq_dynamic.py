from flask import Flask, render_template
from models.category import Category
from models.quote import Quote
from models.engine.db_storage import DBStorage

app = Flask(__name__)
db_storage = DBStorage()
db_storage.reload()

@app.route('/inspiro_quotes', methods=['GET'], strict_slashes=False)
def show_inspiro_quotes():
    return render_template('inspiro_quotes.html')

@app.teardown_appcontext
def teardown_db(exception):
    """Close database connection."""
    db_storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
