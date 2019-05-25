from django.shortcuts import render, redirect, reverse
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    FormView,
)

from posts.models import Book, Post
from posts.forms import BookForm, PostForm, PostAndBookForm
from posts.services import create_post_and_book

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


def new_post_view(request):
    if request.method == "POST":
        post_form = PostForm(request.POST, prefix="post_form")
        book_form = BookForm(request.POST, prefix="book_form")
        
        if post_form.is_valid() and book_form.is_valid():
            create_post_and_book(post=post_form, book=book_form)

    else:
        post_form = PostForm(prefix="post_form")
        book_form = BookForm(prefix="book_form")
        context = {"post_form": post_form, "book_form": book_form}
    return render(request, "posts/post_form.html", context=context)

class NewPostAndBookView(FormView):
    template_name = "posts/post_form.html"
    form_class = PostAndBookForm
    success_url = '/'

    def form_valid(self, form):
        user = self.request.user
        print(user)
        create_post_and_book(form=form, user=user)
        return super().form_valid(form)