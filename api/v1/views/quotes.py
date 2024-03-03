#!/usr/bin/python3
"""Module containing API routes for Quote objects."""
from api.v1.views import app_views
from flask import jsonify, abort, make_response, request
from models.engine.db_storage import storage
from models.category import Category
from models.quote import Quote
from models.author import Author
import datetime


@app_views.route('/quotes', methods=['GET'], strict_slashes=False)
def get_all_quotes():
    """Get all Quote objects."""
    all_quotes = storage.all(Quote)
    return jsonify([quote.to_dict() for quote in all_quotes.values()])

@app_views.route('/daily_quote', methods=['GET'], strict_slashes=False)
def quote_of_the_day():

    all_quotes = storage.all(Quote).values()

    if not all_quotes:
        return jsonify({"error": "No quotes available"}), 404

    current_date = datetime.datetime.now()
    day_of_year = current_date.timetuple().tm_yday

    quote_list = list(all_quotes)
    quote_index = day_of_year % len(quote_list)
    selected_quote = quote_list[quote_index]

    author = storage.get(Author, selected_quote.author_id)
    if author is None:
        abort(404)

    quote_dict = selected_quote.to_dict()
    quote_dict['author_name'] = author.name

    return jsonify(quote_dict)


@app_views.route('/categories/<category_id>/quotes', methods=['GET'], strict_slashes=False)
def get_quotes_by_category(category_id):
    category = storage.get(Category, category_id)
    if category is None:
        abort(404)
    quotes_with_authors = []
    for quote in category.quotes:
        quote_dict = quote.to_dict()
        quote_dict['author_name'] = quote.author.name
        quotes_with_authors.append(quote_dict)
    return jsonify(quotes_with_authors)

@app_views.route('/authors/<author_id>/quotes', methods=['GET'], strict_slashes=False)
def get_quotes_by_author(author_id):
    """Get all Quote objects by author ID."""
    # Assuming you have an 'Author' model with a 'quotes' relationship defined
    author = storage.get(Author, author_id)
    if author is None:
        abort(404)  # Author not found
    
    # Utilize the relationship between Author and Quote to fetch associated quotes
    quotes = author.quotes if hasattr(author, 'quotes') else []
    return jsonify([quote.to_dict() for quote in quotes])

@app_views.route('/quotes/<quote_id>', methods=['GET'], strict_slashes=False)
def get_quote(quote_id):
    """Get a Quote object by id"""
    quote = storage.get(Quote, quote_id)
    if quote is None:
        abort(404)
    return jsonify(quote.to_dict())


@app_views.route('/quotes/<string:quote_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_quote(quote_id):
    """Delete a Quote object by id."""
    quote = storage.get(Quote, quote_id)
    if quote is None:
        abort(404)
    quote.delete()
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/categories/<category_id>/quotes',
                 methods=['POST'], strict_slashes=False)
def create_quote(category_id):
    """Create a Quote object."""
    category = storage.get(Category, category_id)
    if category is None:
        abort(404)

    data = request.get_json()
    if not data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    if 'text' not in data:
        return make_response(jsonify({"error": "Missing text"}), 400)

    new_quote = Quote(category_id=category_id, **data)
    new_quote.save()
    return jsonify(new_quote.to_dict()), 201


@app_views.route('/quotes/<quote_id>', methods=['PUT'], strict_slashes=False)
def update_quote(quote_id):
    """Update a Quote object."""
    quote = storage.get(Quote, quote_id)
    if quote is None:
        abort(404)

    data = request.get_json()
    if not data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)

    for key, value in data.items():
        if key not in ['id', 'category_id', 'created_at', 'updated_at']:
            setattr(quote, key, value)

    quote.save()
    return jsonify(quote.to_dict())
