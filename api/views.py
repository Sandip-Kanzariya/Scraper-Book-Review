from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from flask_restful import Api
from marshmallow import ValidationError
from api.resources import book
from api.resources import review

book_blueprint = Blueprint("book", __name__, url_prefix="/")
api = Api(book_blueprint, errors=book_blueprint.errorhandler)


# 
api.add_resource(book.BookList, "/books")
api.add_resource(review.ReviewList, "/books/<int:book_id>/reviews")

@book_blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    return jsonify(e.messages), 400


