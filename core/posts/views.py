from django.shortcuts import render,redirect,reverse
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
    post_form = PostForm
    book_form = BookForm
    context = {
        "post_form": post_form,
        "book_form":book_form,
    }
    return render(request, 'posts/post_form.html', context=context)