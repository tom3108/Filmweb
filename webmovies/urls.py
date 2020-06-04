from django.urls import path
from . import views
from . views import (
	MovieListView,
	MovieCreateView, 
	MovieDetailView,
	MovieUpdateView,
	

)

urlpatterns = [
	path('main/', MovieListView.as_view() , name = 'web-movie'), 
	path('new/', MovieCreateView.as_view() , name = 'web-new'),
	path('mov/<int:pk>/', MovieDetailView.as_view() , name = 'web-det'),
	path('mov/<int:pk>/update', MovieUpdateView.as_view() , name = 'web-update'),


]