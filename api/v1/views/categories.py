#!/usr/bin/python3
"""Module containing API routes for Category objects."""
from api.v1.views import app_views
from flask import jsonify, abort, make_response, request
from models.engine.db_storage import storage
from models.category import Category


@app_views.route('/categories', methods=['GET'], strict_slashes=False)
def get_all_categories():
    """Get all Category objects."""
    all_categories = storage.all(Category).values()
    list_categories = []
    for category in all_categories:
        list_categories.append(category.to_dict())
    return jsonify(list_categories)


@app_views.route('/categories/<category_id>',
                 methods=['GET'], strict_slashes=False)
def get_category(category_id):
    """Get a Category object by id"""
    category = storage.get(Category, category_id)
    if category is None:
        abort(404)
    return jsonify(category.to_dict())


@app_views.route('/categories/<string:category_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_category(category_id):
    """Delete a Category object by id."""
    category = storage.get(Category, category_id)
    if category is None:
        abort(404)
    category.delete()
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/categories/', methods=['POST'], strict_slashes=False)
def create_category():
    """Create a Category object."""
    data = request.get_json()
    if not data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    if 'name' not in data:
        return make_response(jsonify({"error": "Missing name"}), 400)
    new_category = Category(**data)
    new_category.save()
    return jsonify(new_category.to_dict()), 201


@app_views.route('/categories/<category_id>',
                 methods=['PUT'], strict_slashes=False)
def update_category(category_id):
    """Update a Category object."""
    category = storage.get(Category, category_id)
    if category is None:
        abort(404)
    data = request.get_json()
    if not data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)

    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(category, key, value)

    category.save()
    return jsonify(category.to_dict())
