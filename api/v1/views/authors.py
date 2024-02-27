#!/usr/bin/python3
"""Module containing API routes for Author objects."""
from api.v1.views import app_views
from flask import jsonify, abort, make_response, request
from models.engine.db_storage import storage
from models.author import Author


@app_views.route('/authors', methods=['GET'], strict_slashes=False)
def retrieve_all_authors():
    """Get all Author objects."""
    all_authors = storage.all(Author).values()
    list_authors = []
    for author in all_authors:
        list_authors.append(author.to_dict())
    return jsonify(list_authors)


@app_views.route('/authors/<author_id>', methods=['GET'], strict_slashes=False)
def retrieve_author(author_id):
    """Get an Author object by id."""
    author = storage.get(Author, author_id)
    if author is None:
        abort(404)
    return jsonify(author.to_dict())


@app_views.route('/authors/<string:author_id>', methods=['DELETE'], strict_slashes=False)
def remove_author(author_id):
    """Delete an Author object by id."""
    author = storage.get(Author, author_id)
    if author is None:
        abort(404)
    author.delete()
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/authors/', methods=['POST'], strict_slashes=False)
def make_author():
    """Create an Author object."""
    data = request.get_json()
    if not data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    if 'name' not in data:
        return make_response(jsonify({"error": "Missing name"}), 400)
    new_author = Author(**data)
    new_author.save()
    return jsonify(new_author.to_dict()), 201


@app_views.route('/authors/<author_id>', methods=['PUT'], strict_slashes=False)
def renew_author(author_id):
    """Update an Author object."""
    author = storage.get(Author, author_id)
    if author is None:
        abort(404)
    data = request.get_json()
    if not data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)

    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(author, key, value)

    author.save()
    return jsonify(author.to_dict())
