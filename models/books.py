from extensions import db  
from extensions import db

class Book(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    author = db.Column(db.String(500))
    book_link = db.Column(db.String(500))
    cover_link = db.Column(db.String(500))
    
    reviews = db.relationship('Review', backref='book', lazy=True)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text)
    rating = db.Column(db.Integer)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)


