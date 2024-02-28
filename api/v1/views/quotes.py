#!/usr/bin/python3
"""Module containing API routes for Quote objects."""
from api.v1.views import app_views
from flask import jsonify, abort, make_response, request
from models.engine.db_storage import storage
from models.category import Category
from models.quote import Quote
import datetime


@app_views.route('/quotes', methods=['GET'], strict_slashes=False)
def get_all_quotes():
    """Get all Quote objects."""
    all_quotes = storage.all(Quote)
    return jsonify([quote.to_dict() for quote in all_quotes.values()])

@app_views.route('/daily_quote', methods=['GET'], strict_slashes=False)
def quote_of_the_day():
    # Get all quotes
    all_quotes = storage.all(Quote)
    
    # Calculate the current day of the year
    current_date = datetime.datetime.now()
    day_of_year = current_date.timetuple().tm_yday
    
    # Use the current day to index into the list of quotes
    quote_index = day_of_year % len(all_quotes)
    
    # Get the quote of the day
    quote = list(all_quotes.values())[quote_index]
    
    return jsonify(quote.to_dict())

@app_views.route('/categories/<category_id>/quotes',
                 methods=['GET'], strict_slashes=False)
def get_quotes_by_category(category_id):
    """Get all Quote objects of a Category."""
    list_quotes = []
    category = storage.get(Category, category_id)
    if category is None:
        abort(404)

    for quote in category.quotes:
        list_quotes.append(quote.to_dict())
    return jsonify(list_quotes)


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
