from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from extensions import db
from models.books import Book
from models.books import Review
from models.books import Review

class ReviewList(Resource):

    def get(self, book_id):
        page = request.args.get('page', default=1, type=int)
        size = request.args.get('size', default=10, type=int)
        
        book = Book.query.get(book_id)
        if not book:
            return {'message': 'Book not found'}, 404
        
        reviews = Review.query.filter_by(book_id=book_id).paginate(page=page, per_page=size)
        
        response = {
            'reviews': [],
            'total_pages': reviews.pages,
            'current_page': reviews.page,
            'total_reviews': reviews.total
        }
        
        for review in reviews.items:
            response['reviews'].append({
                'id': review.id,
                'rating': review.rating,
                'comment': review.comment
            })
        
        return response, 200
    
    def post(self, book_id):
        data = request.get_json()
        comment = data.get('comment')
        rating = int(data.get('rating'))
        
        book = Book.query.get(book_id)
        if not book:
            return {'message': 'Book not found'}, 404

        review = Review(rating=rating, comment=comment, book_id=book_id)
        db.session.add(review)

        db.session.commit()
        
        return {'message': 'Review created successfully'}, 201
    
