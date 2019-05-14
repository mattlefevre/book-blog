from django.shortcuts import render
from django.views.generic import (
    CreateView,DeleteView, DetailView, ListView, 
    UpdateView,
)

from posts.models import Post

# Create your views here.
class PostCreateView(CreateView):
    model = Post
    fields = [
        'post_title',
        'post_contents',
    ]

class PostDeleteView(DeleteView):
    model = Post

class PostDetailView(DetailView):
    model = Post

class PostListView(ListView):
    model = Post 
    paginate_by = 20

class PostUpdateView(UpdateView):
    model = Post