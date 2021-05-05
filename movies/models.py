from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=500)
    release_date = models.DateField()
    directed_by = models.CharField(max_length=50)
    series_name = models.CharField(max_length=50)
    movie_order = models.IntegerField()
    str

