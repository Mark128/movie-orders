from django.contrib import admin
from .models import Movie, Series, Genre


class MoviesAdmin(admin.ModelAdmin):
    model = Movie
    list_display = ['name', 'series', 'movie_order', 'image']
    fields = ['name', 'release_date', 'series', 'movie_order', 'image']


class SeriesAdmin(admin.ModelAdmin):
    model = Series
    list_display = ['name', 'description', 'get_genre']
    fields = ['name', 'description', 'genre']

    def get_genre(self, obj):
        return obj.genre.name

    get_genre.short_description = 'Genre'
    get_genre.admin_order_field = 'genre__name'


class GenreAdmin(admin.ModelAdmin):
    model = Genre
    list_display = ['name']
    fields = ['name']


admin.site.register(Movie, MoviesAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Genre, GenreAdmin)

