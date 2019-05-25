"""Holds the business logic of Posts. This is for converting input into 
ORM objects. """
from posts.models import Book, Post
from django import forms
# from posts.forms import PostAndBookForm
 

def no_book_check(*, form:"PostAndBookForm"):
    if form['author'] == "":
        print("No Author")
        return True
    if form['title'] == "":
        print("No title")
        return True
    return False

def create_post_and_book(*, form:"PostAndBookForm", user):
    if form.is_valid():
        print("The form was valid")
        poster = user
        post_title = form.cleaned_data['post_title']
        post_contents = form.cleaned_data['post_contents']

        # book_check: Boolean field that is true when checked. 
        # "True" is equivelant to "No book"
        
        author = form.cleaned_data['author']
        title = form.cleaned_data['title']
        synopsis = form.cleaned_data['synopsis']
        cover_image = form.cleaned_data['cover_image']
        isbn = form.cleaned_data['isbn']
        rating = form.cleaned_data['rating']
        if not no_book_check(form=form.cleaned_data):
            # Save with book
            book_to_db = Book(author=author, title=title,synopsis=synopsis, cover_image=cover_image,
            isbn=isbn, rating=rating)
            book_to_db.save()
            post_to_db = Post(post_title=post_title, post_contents=post_contents, book=book_to_db)
            print("This should be posting both to the database.")
        else:
            post_to_db = Post(post_title=post_title, post_contents=post_contents)
            print("This should be at least posting the Post to the database.")
        print("Made it here.")
        post_to_db.poster = user
        post_to_db.save()
    return forms.ValidationError("Something went wrong with create_and_post_book")