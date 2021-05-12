from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name


class Series(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=500)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='movie_genres')

    def __str__(self):
        return self.name


def movie_image_path(instance, filename):
    series = str(instance.series.name).replace(" ", "_")
    return 'movies/static/movies/img/{0}/{1}'.format(series, filename)


class Movie(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=500)
    release_date = models.DateField()
    directed_by = models.CharField(max_length=50)
    series = models.ForeignKey(Series, on_delete=models.PROTECT, related_name='movie_to_series')
    movie_order = models.IntegerField(null=True)
    image = models.ImageField(upload_to=movie_image_path, height_field=None, width_field=None, max_length=100, null=True)

    def __str__(self):
        return self.name






