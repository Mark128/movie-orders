from django.http import HttpResponse, Http404
from django.shortcuts import render

from movies.models import Movie, Series, Genre


def series(request):
    series_list = Series.objects.all().order_by('name')

    genres = Genre.objects.all().order_by('name')
    output = {
        'genres': genres,
        'series': series_list
    }
    # TODO: get from-to date for whole series

    return render(request, 'movies/series.html', output)


def series_detail(request, series_name):
    movie_list = Movie.objects.filter(series__short_name=series_name).order_by('release_date')
    output = {'movie_list': movie_list}
    return render(request, 'movies/movies.html', output)


def details(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist")

    output = {
        'movie': movie
    }

    return render(request, 'movies/movie-details.html', output)
