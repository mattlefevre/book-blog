from django import forms
from posts.models import Book, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["post_title", "post_contents"]


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ["author", "title", "isbn", "cover_image", "synopsis", "rating"]
        widgets = {
            "cover_image": forms.FileInput(attrs={"class": "buttontest"}),
            "rating": forms.RadioSelect(choices=(1,2,3,4,5))
        }


class PostAndBookForm(forms.Form):
    # Post
    post_title = forms.CharField(label="Post Title", max_length=100)
    post_contents = forms.CharField(label="Post Contents", widget=forms.Textarea)
    # Book
    author = forms.CharField(label="Author", max_length=50)
    title = forms.CharField(label="Book's Title", max_length=100)
    isbn = forms.CharField(max_length=20)
    cover_image = forms.ImageField()
    synopsis = forms.CharField(label="Synopsis", required=False, widget=forms.Textarea)
    rating = forms.CharField(label="Rating",
        widget=forms.Select(choices=((1,1),(2,2),(3,3),(4,4),(5,5))), required=False)