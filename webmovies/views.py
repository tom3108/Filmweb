from django.shortcuts import render
from .models import Movie 

def movie (request):
	movies = Movie.objects.all()
	return render (request, 'webmovies/movies.html', {'movies':movies})

# Create your views here.
