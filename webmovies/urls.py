from django.urls import path
from . import views

urlpatterns = [
	path('movie/', views.movie , name = 'web-movie')
]