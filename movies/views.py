from django.http import HttpResponse, Http404
from django.shortcuts import render

from movies.models import Movie


def all_movies(request):
    movie_list = Movie.objects.all().order_by('name')
    output = {
        'movies': movie_list
    }

    return render(request, 'movies/all-movies.html', output)


def details(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist")

    output = {
        'movie': movie
    }

    return render(request, 'movies/movie-details.html', output)
