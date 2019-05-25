"""Holds the business logic of Posts. This is for converting input into 
ORM objects. """
from posts.models import Book, Post
from posts.forms import PostAndBookForm


def include_book(*, form:PostAndBookForm):
    pass

def create_post_and_book(*, form:PostAndBookForm):
    if form.is_valid():
        post_to_db = Post()
        post_to_db['post_title'] = form['post_title']
        post_to_db['post_contents'] = form['post_contents']

    if include_book():
        book_to_db = Book()
        book_to_db['author'] = form['author']
        book_to_db['title'] = form['title']
        book_to_db['synopsis'] = form['synopsis']
        book_to_db['cover_image'] = form['cover_image']
        book_to_db['isbn'] = form['isbn']
        book_to_db['rating'] = form['rating']