from extensions import ma
from models.books import Book


# This Schema for Returing the zeelab data
class BookSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Book
        load_instance = True # Load the instance of the model : Use for update
        