from django.contrib import admin
from .models import Movie

#admin.site.register(Movie)

@admin.register(Movie)
class MovieAdmin (admin.ModelAdmin):
	#fields = ["title", "year", "descript"]
	#exclude = ["descript"]
	#list_display = ["title", 'year', 'imdb_rating' ]
	#list_filter = ['year']
	search_fields = ["title"]

