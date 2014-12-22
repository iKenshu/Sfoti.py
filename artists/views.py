from django.shortcuts import render
from .models import Artist
from django.views.generic import DetailView

class ArtistDetailView(DetailView):
	template_name = 'artist.html'
	model = Artist
	context_object_name = 'artist'