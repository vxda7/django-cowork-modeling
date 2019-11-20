from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=20)


class Movie(models.Model):
    title = models.CharField(max_length=30)
    audience = models.IntegerField()
    poster_url = models.CharField(max_length=140)
    description = models.TextField()
    genres = models.ManyToManyField(Genre, related_name='movies')
    like_users = models.ManyToManyField(
        get_user_model(), related_name='like_movies')


class Review(models.Model):
    content = models.CharField(max_length=140)
    score = models.IntegerField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
