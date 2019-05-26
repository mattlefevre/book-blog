from django.urls import path
from users.views import PosterDetailView, PostersListView

app_name = "users"

urlpatterns = [
    path('', PostersListView.as_view(), name='reviewers'),
    path('<int:pk>/<str:username>', PosterDetailView.as_view(), name='individual_reviewer'),
]