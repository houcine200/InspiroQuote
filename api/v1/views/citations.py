#!/usr/bin/python3
"""Module containing API routes for Citation objects."""
from api.v1.views import app_views
from flask import jsonify, abort, make_response, request
from models.engine.db_storage import storage
from models.author import Author
from models.citation import Citation


@app_views.route('/authors/<author_id>/citations',
                 methods=['GET'], strict_slashes=False)
def get_citations_by_author(author_id):
    """Get all Citation objects of an Author."""
    list_citations = []
    author = storage.get(Author, author_id)
    if author is None:
        abort(404)

    for citation in author.citations:
        list_citations.append(citation.to_dict())
    return jsonify(list_citations)


@app_views.route('/citations/<citation_id>', methods=['GET'], strict_slashes=False)
def get_citation(citation_id):
    """Get a Citation object by id"""
    citation = storage.get(Citation, citation_id)
    if citation is None:
        abort(404)
    return jsonify(citation.to_dict())


@app_views.route('/citations/<string:citation_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_citation(citation_id):
    """Delete a Citation object by id."""
    citation = storage.get(Citation, citation_id)
    if citation is None:
        abort(404)
    citation.delete()
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/authors/<author_id>/citations',
                 methods=['POST'], strict_slashes=False)
def create_citation(author_id):
    """Create a Citation object."""
    author = storage.get(Author, author_id)
    if author is None:
        abort(404)

    data = request.get_json()
    if not data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    if 'text' not in data:
        return make_response(jsonify({"error": "Missing text"}), 400)

    new_citation = Citation(author_id=author_id, **data)
    new_citation.save()
    return jsonify(new_citation.to_dict()), 201


@app_views.route('/citations/<citation_id>', methods=['PUT'], strict_slashes=False)
def update_citation(citation_id):
    """Update a Citation object."""
    citation = storage.get(Citation, citation_id)
    if citation is None:
        abort(404)

    data = request.get_json()
    if not data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)

    for key, value in data.items():
        if key not in ['id', 'author_id', 'created_at', 'updated_at']:
            setattr(citation, key, value)

    citation.save()
    return jsonify(citation.to_dict())