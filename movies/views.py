from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Genre, Review
from django.contrib.auth import get_user_model
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)


def detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    reviews = movie.review_set.order_by('-id')
    form = ReviewForm()
    context = {
        'movie': movie,
        'form': form,
        'reviews': reviews
    }
    return render(request, 'movies/detail.html', context)

@login_required
def new(request, id):
    movie = get_object_or_404(Movie, id=id)
    user = request.user
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = user
            review.save()

            return redirect('movies:detail', movie.id)
    else:
        return redirect('movies:index')



def delete(request, id, review_id):
    review = get_object_or_404(Review, id=review_id)
    review.delete()
    return redirect('movies:detail', id)


@login_required
def like(request, id):
    movie = get_object_or_404(Movie, id=id)
    user = request.user
    if request.method == "POST":
        if movie.like_users.filter(id=user.id):
            movie.like_users.remove(user)
        else:
            movie.like_users.add(user)
        return redirect('movies:detail', id)