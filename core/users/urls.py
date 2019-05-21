from django.urls import path
from users.views import PosterDetailView, PostersListView


urlpatterns = [
    path('', PostersListView.as_view(), name='reviewers'),
    path('<str:username>-<int:pk>', PosterDetailView.as_view(), name='reviewer'),
]