"""Holds the business logic of Posts. Functions here should only be helping to convert input into 
ORM objects. """

from posts.models import Book, Post
from django import forms
from users.models import CustomUser

# from posts.forms import PostAndBookForm


def book_excluded_check(*, form: "BookForm") -> bool:
    if form["author"] == "" and form["title"] == "":
        return True
    return False


def no_book_check(*, form: "PostAndBookForm") -> bool:
    if form["author"] == "":
        print("No Author")
        return True
    if form["title"] == "":
        print("No title")
        return True
    return False


def create_post_and_book(*, form: "PostAndBookForm", user: CustomUser) -> None:
    """ 
    Function for creating BOTH a new Post row and Book row in the database.
    """

    if form.is_valid():
        # Post Fields
        poster = user
        post_title = form.cleaned_data["post_title"]
        post_contents = form.cleaned_data["post_contents"]
        image = form.cleaned_data["image"]
        # Book Fields
        author = form.cleaned_data["author"]
        title = form.cleaned_data["title"]
        synopsis = form.cleaned_data["synopsis"]
        isbn = form.cleaned_data["isbn"]
        rating = form.cleaned_data["rating"]

        if no_book_check(form=form.cleaned_data):
            post_to_db = Post(post_title=post_title, post_contents=post_contents, image=image)
        else:
            # Save with book
            book_to_db = Book(
                author=author,
                title=title,
                synopsis=synopsis,
                isbn=isbn,
                rating=rating,
            )
            book_to_db.save()
            post_to_db = Post(post_title=post_title, post_contents=post_contents, book=book_to_db, image=image) 
        
        post_to_db.poster = user
        post_to_db.save()
    return forms.ValidationError("Something went wrong with create_and_post_book")

def book_already_exists(author, title):
    #NOTE: Not quite done here.
    try:
        existing_book = Book.objects.get(author=author, title=title)
    finally:
        print(existing_book)