from django.urls import path
from users.views import PosterDetailView, PosterListView


urlpatterns = [
    path('', PosterListView.as_view(), 'reviewers'),
    path('<str:username>', PosterDetailView.as_view(), name='about'),

]