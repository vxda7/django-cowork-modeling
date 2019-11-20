from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Genre
from django.contrib.auth import get_user_model
# Create your views here.

def index(request):
    
    return render(request, 'movies/index.html')


def detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)