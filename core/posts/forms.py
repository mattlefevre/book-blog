from django.forms import ModelForm, CharField, FileInput
from posts.models import Book, Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["post_title", "post_contents"]


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["author", "title", "cover_image", "isbn"]

        widgets = {"cover_image": FileInput(attrs={"class": "buttontest"})}
