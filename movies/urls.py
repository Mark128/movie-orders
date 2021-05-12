from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.series, name='index'),
    path('all-movies/', views.series, name='all-movies'),
    path('<int:movie_id>/', views.details, name='details')
]
