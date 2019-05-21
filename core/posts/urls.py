from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from posts.views import (
    BookListView,
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostListView,
    PostUpdateView,
    new_post,
)

# NOTE: URL permisisons are being set in this file where applicable. /
# NOTE: Note the "login_required" functions in each appropriate each path().

urlpatterns = [
    path("", PostListView.as_view(), name="home"),
    path("<str:username>/<str:slug>/", PostDetailView.as_view(), name="review"),
    path("new_post/", login_required(new_post), name="new_post"),
    # NOTE: I should be able to leave the update_post page as a PostUpdateView because
    # I won't ever need to update which book it's about.
    path("update_post/", login_required(PostUpdateView.as_view()), name="update_post"),
    path("books/", BookListView.as_view(), name="books"),
]
