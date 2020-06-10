from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Movie, Genre
from tmdb_data import get_movie_poster, get_movie_video, get_movie_data


def index(request):
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    return render(request, 'movies/index.html', {'movies': movies, 'genres': genres})


def filter_genre(request, genre_id):
    movies = Movie.objects.filter(genre=genre_id)
    genres = Genre.objects.all()
    return render(request, 'movies/index.html', {'movies': movies, 'genres': genres})


def detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    poster = get_movie_poster(movie.tmdb_id)
    video = get_movie_video(movie.tmdb_id)
    movie_budget = get_movie_data(movie.tmdb_id, 'budget')
    return render(request, 'movies/detail.html', {'movie': movie, 'movie_poster': poster, 'video_key': video, 'movie_budget': movie_budget})
