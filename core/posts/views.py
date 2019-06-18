from django.shortcuts import render, redirect, reverse
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    FormView,
)
from django.urls import reverse, reverse_lazy

from core.posts.models import Book, Post
from core.posts.forms import BookForm, PostForm, PostAndBookForm
from core.posts.services import create_post_and_book, book_excluded_check, no_book_check

# Create your views here.
class PostCreateView(CreateView):
    model = Post
    fields = [
        "post_title",
        "post_contents",
        "book.author",
        "book.title",
        "book.synopsis",
        "book.cover_image",
        "book.isbn",
        "book.rating",
    ]


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("posts:home")


class PostDetailView(DetailView):
    model = Post


class PostListView(ListView):
    model = Post
    paginate_by = 20


class PostUpdateView(UpdateView):

    model = Post
    form_class = PostForm
    success_url = reverse_lazy("posts:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["book"] = self.object.book
        return context


class BookUpdateView(UpdateView):

    model = Book
    form_class = BookForm
    success_url = reverse_lazy("posts:home")


class BookListView(ListView):
    model = Book


class NewPostAndBookView(FormView):
    template_name = "posts/create_post_form.html"
    form_class = PostAndBookForm
    success_url = "/"

    def form_valid(self, form):
        user = self.request.user
        print(user)
        create_post_and_book(form=form, user=user)
        return super().form_valid(form)
