from rest_framework import viewsets

from .models import *
from .serializer import *


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class AutorViewSet(viewsets.ModelViewSet):
	queryset = Autor.objects.all()
	serializer_class = AutorSerializer

class LibroViewSet(viewsets.ModelViewSet):
	queryset = Libro.objects.all()
	serializer_class = LibroSerializer

	def get_queryset(self):
		"""
		Optionally restricts the returned purchases to a given user,
		by filtering against a `username` query parameter in the URL.
		"""
		queryset = Libro.objects.all()
		autor = self.request.query_params.get('autor', None)
		if autor is not None:
			libros = map(lambda pair: pair.id_libro.id_libro, Autor_Libro.objects.filter(id_autor=autor))
			queryset = Libro.objects.filter(pk__in=libros)
		return queryset

class PersonaViewSet(viewsets.ModelViewSet):
	queryset = Persona.objects.all()
	serializer_class = PersonaSerializer

class RateViewSet(viewsets.ModelViewSet):
	queryset = Rate.objects.all()
	serializer_class = RateSerializer

class AutorLibroViewSet(viewsets.ModelViewSet):
	queryset = Autor_Libro.objects.all()
	serializer_class = AutorLibroSerializer
