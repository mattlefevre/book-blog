from django.shortcuts import render
from django.views.generic import ListView, DetailView
from users.models import CustomUser

# Create your views here.

class PostersListView(ListView):
    model = CustomUser
    template_name = "users/reviewers_list.html"

class PosterDetailView(DetailView):
    model = CustomUser
    template_name = "users/reviewer_detail.html"
    context_object_name = "poster"