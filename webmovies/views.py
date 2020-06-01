from django.shortcuts import render

def movie (request):
	return render (request, 'webmovies/movies.html')

# Create your views here.
