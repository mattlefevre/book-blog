from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from posts.views import (
    PostCreateView, PostDeleteView,
    PostDetailView, PostListView,
    PostUpdateView
)

# NOTE: URL permisisons are being set in this file. Note the login_required functions
# NOTE: in each path().

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('new_post/', login_required(PostCreateView.as_view()), name='new_post'),
    path('update_post/', login_required(PostUpdateView.as_view()), name="update_post"),
]