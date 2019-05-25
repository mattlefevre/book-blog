"""Holds the business logic of Posts. This is for converting input into 
ORM objects. """
from posts.models import Book, Post
from posts.forms import PostAndBookForm


def book_field_check(*, form:PostAndBookForm):
    if not form['author']:
        return False
    if not form['title']:
        return False
    return True

def create_post_and_book(*, form:PostAndBookForm):
    if form.is_valid():
        post_to_db = Post()
        post_to_db['post_title'] = form['post_title']
        post_to_db['post_contents'] = form['post_contents']

        # book_check: Boolean field that is true when checked. 
        # "True" is equivelant to "No book"
        if not form['book_check'] and book_field_check(form=form):
            book_to_db = Book()
            book_to_db['author'] = form['author']
            book_to_db['title'] = form['title']
            book_to_db['synopsis'] = form['synopsis']
            book_to_db['cover_image'] = form['cover_image']
            book_to_db['isbn'] = form['isbn']
            book_to_db['rating'] = form['rating']