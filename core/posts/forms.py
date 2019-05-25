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
    post_title = forms.CharField(label="Post Title", max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    post_contents = forms.CharField(label="Post Contents", widget=forms.Textarea(attrs={"class":"form-control"}))
    # Book-Check
    book_check = forms.BooleanField(required=False, label="This post isn't about a book", widget=forms.CheckboxInput(attrs={"class":"form-check-input"}))
    # Book
    author = forms.CharField(label="Author", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    title = forms.CharField(label="Book's Title", max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    isbn = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"class":"form-control"}))
    cover_image = forms.ImageField(widget=forms.ClearableFileInput(attrs={"class":"form-control-file"}))
    synopsis = forms.CharField(label="Synopsis", required=False, widget=forms.Textarea(attrs={"class":"form-control"}))
    rating = forms.CharField(label="Rating",
        widget=forms.Select(choices=((1,1),(2,2),(3,3),(4,4),(5,5)),attrs={"class":"form-control"}), required=False)

