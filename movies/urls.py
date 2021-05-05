from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_movies(), name='index'),
    path('all-movies/', views.all_movies, name='all-movies'),
    path('<int:movie_id>/', views.details, name='details')
]
