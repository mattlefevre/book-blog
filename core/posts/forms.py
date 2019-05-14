from django.forms import ModelForm
from posts.models import Book, Post


class PostForm(ModelForm):
    model = Post
    fields = ["post_title", "post_contents"]


class BookForm(ModelForm):
    model = Book
    fields = ["author", "title", "cover_image", "isbn"]
