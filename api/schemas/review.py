from extensions import ma
from models.books import Book
from models.books import Review

# This Schema for Returing the zeelab data
class ReviewSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Review
        load_instance = True # Load the instance of the model : Use for update
        