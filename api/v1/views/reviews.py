#!/usr/bin/python3
"""Module containing API routes for Review objects."""
from api.v1.views import app_views
from flask import jsonify, abort, make_response, request
from models.engine.db_storage import storage
from models.user import User
from models.review import Review
import datetime


@app_views.route('/reviews', methods=['GET'], strict_slashes=False)
def retrieve_all_reviews():
    """Get all Review objects."""
    all_reviews = storage.all(Review)
    return jsonify([review.to_dict() for review in all_reviews.values()])


@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def retrieve_review(review_id):
    """Get a Review object by id"""
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route('/reviews/<string:review_id>',
                 methods=['DELETE'], strict_slashes=False)
def remove_review(review_id):
    """Delete a Review object by id."""
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    review.delete()
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/users/<user_id>/reviews',
                 methods=['GET'], strict_slashes=False)
def retrieve_reviews_by_user(user_id):
    """Get all Review objects of a User."""
    list_reviews = []
    user = storage.get(User, user_id)
    if user is None:
        abort(404)

    for review in user.reviews:
        list_reviews.append(review.to_dict())
    return jsonify(list_reviews)


@app_views.route('/reviews/<string:review_id>',
                 methods=['PUT'], strict_slashes=False)
def renew_review(review_id):
    """Update a Review object."""
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)

    data = request.get_json()
    if not data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)

    for key, value in data.items():
        if key not in ['id', 'user_id', 'created_at', 'updated_at']:
            setattr(review, key, value)

    review.save()
    return jsonify(review.to_dict())


@app_views.route('/users/<user_id>/reviews',
                 methods=['POST'], strict_slashes=False)
def make_review(user_id):
    """Create a Review object."""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)

    data = request.get_json()
    if not data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    if 'text' not in data:
        return make_response(jsonify({"error": "Missing text"}), 400)

    new_review = Review(user_id=user_id, **data)
    new_review.save()
    return jsonify(new_review.to_dict()), 201
