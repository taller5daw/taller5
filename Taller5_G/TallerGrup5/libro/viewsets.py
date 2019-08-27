from rest_framework import viewsets

from .models import *
from .serializer import *


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class AutorViewSet(viewsets.ModelViewSet):
	queryset = Autor.objects.all()
	serializer_class = AutorSerializer

	def get_queryset(self):
		queryset = Autor.objects.all()
		libro = self.request.query_params.get('libro', None)
		if libro is not None:
			autores = map(lambda pair: pair.id_autor.id_autor, Autor_Libro.objects.filter(id_libro=libro))
			queryset = Autor.objects.filter(pk__in=autores)
		return queryset

class LibroViewSet(viewsets.ModelViewSet):
	queryset = Libro.objects.all()
	serializer_class = LibroSerializer

	def get_queryset(self):
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

	def get_queryset(self):
		queryset = Rate.objects.all()
		user = self.request.query_params.get('user', None)
		libro = self.request.query_params.get('libro', None)
		if user is not None and libro is not None:
			queryset = Rate.objects.filter(user=user, id_libro=libro)
		return queryset

class AutorLibroViewSet(viewsets.ModelViewSet):
	queryset = Autor_Libro.objects.all()
	serializer_class = AutorLibroSerializer
