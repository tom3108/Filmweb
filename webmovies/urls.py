from django.urls import path
from . import views
from . views import (
	MovieListView,
	MovieCreateView
)

urlpatterns = [
	path('movie/', MovieListView.as_view() , name = 'web-movie'), 
	path('new/', MovieCreateView.as_view() , name = 'web-new')

]