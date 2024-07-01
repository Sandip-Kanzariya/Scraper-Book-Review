from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from bs4 import BeautifulSoup
import requests
from extensions import db


# http://127.0.0.1:5050/books/
class BookList(Resource):
    
    def get(self):
        return {"message": "Welcome to Book List"}

    def post(self):
        book_link_list = []
        book_title_list = []
        book_author_list = []
        book_cover_link_list = []

        for i in range(1,5):
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
                    book_cover_link_list.append(book_cover_link);
                    

                    # Etract Details of book 
                    book_details = b.find_all('div', class_='details')
                    # print(book_details[0])
                    book_author = book_details[0].find('span', class_='bookauthor').a.text
                    book_author_list.append(book_author)
                    book_title = book_details[0].find('h3', class_='booktitle').a.text
                    book_title_list.append(book_title)
                    

                results = {}
                results['Title'] = book_title_list
                results['Author'] = book_author_list
                results['BookLink'] = book_link_list
                results['CoverLink'] = book_cover_link_list
        
        return results