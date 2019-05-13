from django.urls import path
from posts.views import (
    PostCreateView, PostDeleteView,
    PostDetailView, PostListView,
    PostUpdateView
)
# TODO: Update above to not include *

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
]