
## Run Project


#### 1. Clone this Repository :

```
git clone https://github.com/Sandip-Kanzariya/Scraper-Book-Review.git
```

## Setting up a Python Virtual Environment and Installing Packages (py = python)

### Create Virtual Environment

```bash
py -m venv .venv
```

### Activate Virtual Environment

```bash
.venv\Scripts\activate
```

### Install Packages From requirements.txt

```bash
pip install -r requirements.txt
```

### Environment Variable Setup (env.env file make changes as per your need)
```py
FLASK_APP=app
FLASK_DEBUG=True
FLASK_RUN_PORT=5050
FLASK_RUN_HOST=0.0.0.0

# For Remote PostgreSQL Database : postgresql://username:password@hostname:port/database_name
SQLALCHEMY_DATABASE_URI=POSTGRESQL_REMOTE_URL
```

### Rest APIs

#### Book 
```

✅POST(Scrping Of Data From Given Website):
=> https://scraper-book-review.onrender.com/books  

✅GET(Get Scrped Data) 
=> https://scraper-book-review.onrender.com/books 
```

#### Reviews
```

✅POST(Create Review for book_id):
=> https://scraper-book-review.onrender.com/books/{book_id}/reviews  

✅GET(Get Review of book with book_id) 
=> https://scraper-book-review.onrender.com/books/{book_id}/reviews

eg. https://scraper-book-review.onrender.com/books/2/reviews
```