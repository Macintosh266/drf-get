from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from app1.views import *

urlpatterns = [
    path('actor/',ActorApi.as_view()),
    path('movie/',MovieApi.as_view()),
    path('actor1/<int:pk>/', ActorUpdate.as_view()),
    path('movie1/<int:pk>/', MovieUpdate.as_view()),
    path('actorsofmovie/', ActorsofMovie.as_view()),
    path('movies_year/<int:year1>/', MoviesYear.as_view()),
    path('movies_year/<int:year1>/<int:year2>/', MoviesYear.as_view()),
    path('commit_movie/', CommentListCreateView.as_view()),
    path('commit_movie/<int:pk>/', CommentDetailView.as_view()),
    ]