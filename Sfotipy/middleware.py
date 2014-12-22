from random import choice
from django.shortcuts import redirect
paises = ['Colombia', 'Mexico', 'Venezuela']

def de_donde_vengo(request):
	return choice(paises)

class PaisMiddleware():
	def process_request(self, request):
		pais = de_donde_vengo(request)
		if pais == 'Venezuela':
			return redirect('http://mejorando.la')