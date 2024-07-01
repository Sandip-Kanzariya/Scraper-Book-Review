from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from bs4 import BeautifulSoup
import requests
from extensions import db
from models.books import Book

# http://127.0.0.1:5050/books/
class BookList(Resource):
    
    
    def get(self):
        # All Scraped Data From Book 
        books = Book.query.all()
        response = []
        for book in books:
            response.append({
                'Title': book.title,
                'Author': book.author,
                'BookLink': book.book_link,
                'CoverLink': book.cover_link
            })
        return response

    def post(self):
        book_link_list = []
        book_title_list = []
        book_author_list = []
        book_cover_link_list = []

        for i in range(1,3):
            url = f"https://openlibrary.org/trending/daily?page={i}"

            webpage=requests.get(url).text

            soup=BeautifulSoup(webpage,'html.parser')


            books=soup.find_all('div',class_='mybooks-list')


            for book in books:
                book_item = book.find_all('div', class_='sri__main')
                

                for b in book_item:
                
                    # Extract Link of Product and link of cover Page 
                    book_cover = b.find_all('span', class_='bookcover')

                    book_link = 'https://openlibrary.org/' + book_cover[0].a['href']
                    book_link_list.append(book_link)

                    book_cover_link = book_cover[0].a.img['src']
                    book_cover_link = book_cover_link.replace('//', '', 1)
                    book_cover_link_list.append(book_cover_link)
                    

                    # Etract Details of book 
                    book_details = b.find_all('div', class_='details')
                    # print(book_details[0])
                    book_author = book_details[0].find('span', class_='bookauthor').a.text
                    book_author_list.append(book_author)
                    book_title = book_details[0].find('h3', class_='booktitle').a.text
                    book_title_list.append(book_title)
                    
                    storebook = Book(
                        title=book_title,
                        author=book_author,
                        book_link=book_link,
                        cover_link=book_cover_link
                    )
                    db.session.add(storebook)
                    db.session.commit()

    
        results = {
            'Title': book_title_list, 
            'Author': book_author_list, 
            'BookLink': book_link_list,
            'CoverLink': book_cover_link_list}


        response = []

        for i in range(len(book_title_list)):
            response.append({
                'Title': book_title_list[i],
                'Author': book_author_list[i],
                'BookLink': book_link_list[i],
                'CoverLink': book_cover_link_list[i]
            }) 


        return response