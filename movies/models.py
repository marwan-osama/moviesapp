from django.db import models
from django.utils import timezone


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    tmdb_id = models.IntegerField()
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    rating = models.FloatField()
    genre = models.ManyToManyField(Genre)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
