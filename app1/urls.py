from django.urls import path
from app1.views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

from rest_framework_simplejwt.views import TokenVerifyView


urlpatterns = [
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/', LoginUser.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
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