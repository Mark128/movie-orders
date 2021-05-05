from django.contrib import admin
from .models import Movie


class MoviesAdmin(admin.ModelAdmin):
    model = Movie
    list_display = ['name', 'series_name', 'movie_order']
    fields = ['name', 'release_date', 'series_name', 'movie_order']


admin.site.register(Movie, MoviesAdmin)

