from extensions import db  

class Book(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300))
    author = db.Column(db.String(200))
    book_link = db.Column(db.String(500))
    cover_link = db.Column(db.String(500))