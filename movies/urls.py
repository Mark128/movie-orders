from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.series, name='index'),
    path('series/<slug:series_name>/', views.series_detail, name='series_detail'),
    path('movies/<int:movie_id>/', views.details, name='movie_detail')
]
