from django.shortcuts import render, redirect, reverse
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from posts.models import Book, Post
from posts.forms import BookForm, PostForm

# Create your views here.
class PostCreateView(CreateView):
    model = Post
    fields = ["post_title", "synopsis", "post_contents", "rating", "book"]


class PostDeleteView(DeleteView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostListView(ListView):
    model = Post
    paginate_by = 20


class PostUpdateView(UpdateView):
    model = Post
    fields = ["post_title", "synopsis", "post_contents", "rating", "book"]


class BookListView(ListView):
    model = Book


def new_post(request):
    if request.method == "POST":
        post_form = PostForm(request.POST, prefix="post_form")
        book_form = BookForm(request.POST, prefix="book_form")
        
        if book_form.is_valid():
            book = Book()
            if book_form["author"] is None:
                pass
                # post the post_form
            elif book_form["author"] is not None:
                # do book stuff
                if post_form.is_valid():
                    post = Post()
                    post.post_title = post_form["post_title"]
                    post.post_contents = post_form["post_contents"]
                    # book - book from above
                else:
                    book = None
                    #return an error - you can't post a book form if the book is wrong
            # return 
        if post_form.is_valid() and book is None:
            pass
            # add logic for a non-book post
    else:
        post_form = PostForm(prefix="post_form")
        book_form = BookForm(prefix="book_form")
        context = {"post_form": post_form, "book_form": book_form}
    return render(request, "posts/post_form.html", context=context)

