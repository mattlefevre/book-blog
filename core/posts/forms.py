from django import forms
from posts.models import Book, Post
from posts.services import no_book_check, create_post_and_book


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
            "rating": forms.Select(choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))),
        }


class PostAndBookForm(forms.Form):
    # Post
    post_title = forms.CharField(
        label="Post Title",
        max_length=100,
        widget=forms.TextInput(attrs={"class": " form-spacing"}),
    )
    post_contents = forms.CharField(
        label="Post Contents", widget=forms.Textarea(attrs={"class": " form-spacing"})
    )
    # Book-Check
    book_check = forms.BooleanField(
        required=False,
        label="This post isn't about a book",
        label_suffix="",
        widget=forms.CheckboxInput(attrs={"class": "book-check"}),
    )
    # Book
    author = forms.CharField(
        required=False,
        label="Author*",
        max_length=50,
        widget=forms.TextInput(attrs={"class": " form-spacing"}),
    )
    title = forms.CharField(
        required=False,
        label="Book's Title*",
        max_length=100,
        widget=forms.TextInput(attrs={"class": " form-spacing"}),
    )
    isbn = forms.CharField(
        required=False,
        max_length=20,
        widget=forms.TextInput(attrs={"class": " form-spacing"}),
    )
    cover_image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={"class": " form-spacing-file"}),
    )
    synopsis = forms.CharField(
        required=False,
        label="Synopsis",
        widget=forms.Textarea(attrs={"class": " form-spacing"}),
    )
    rating = forms.CharField(
        required=False,
        label="Rating",
        widget=forms.Select(
            choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5)),
            attrs={"class": " form-spacing"},
        ),
    )

    # Form Validation, Cleaning, and DB Subitting
    def clean(self):
        cleaned_data = super().clean()
        print(self.cleaned_data["book_check"])
        if self.cleaned_data["book_check"] == False and no_book_check(
            form=self.cleaned_data
        ):
            raise forms.ValidationError(
                "You need to either check the 'This post isn't about a book' box or include book informaiton."
            )
