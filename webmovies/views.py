from django.shortcuts import render
from django.views.generic import (ListView,
	CreateView
	)
from .models import Movie 

def movie (request):
	movies = Movie.objects.all()
	return render (request, 'webmovies/movies.html', {'movies':movies})

class MovieListView(ListView):
	model = Movie 
	template_name = 'webmovies/movies.html'
	context_object_name = 'movies'

class MovieCreateView(CreateView):
	model = Movie 
	fields = ['title', 'descript','year','premiere','poster']

