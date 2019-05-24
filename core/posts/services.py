"""Holds the business logic of Posts. This is for converting input into 
ORM objects. """
from posts.models import Book, Post
from posts.forms import BookForm, PostForm


def create_post_and_book(*, post:PostForm, book:BookForm):
    if post.is_valid():
        if post_test():
            post_to_db = Post()
            post_to_db['post_title'] = post['post_title']
            post_to_db['synopsis'] = post['synopsis']
            post_to_db['post_contents'] = post['post_contents']

        if book.is_valid():
            book_to_db = Book()
            book_to_db['author'] = book['author']
            book_to_db['title'] = book['title']
            book_to_db['cover_image'] = book['cover_image']
            book_to_db['isbn'] = book['isbn']
            book_to_db['rating'] = book['rating']