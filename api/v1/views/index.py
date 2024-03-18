#!/usr/bin/python3
"""Module containing API routes, including the /status route."""
from api.v1.views import app_views
from flask import jsonify
from models.engine.db_storage import storage
from models.category import Category
from models.quote import Quote
from models.author import Author


@app_views.route('/status', strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """Retrieves the number of each object type"""
    stats = {
        "categories": len(storage.all(Category)),
        "quotes": len(storage.all(Quote)),
        "authors": len(storage.all(Author)),
    }
    return jsonify(stats)
