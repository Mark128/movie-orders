from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.all_movies, name='index'),
    path('all-movies/', views.all_movies, name='all-movies'),
    path('<int:movie_id>/', views.details, name='details')
]
