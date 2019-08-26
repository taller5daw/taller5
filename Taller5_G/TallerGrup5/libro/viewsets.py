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

class PersonaViewSet(viewsets.ModelViewSet):
	queryset = Persona.objects.all()
	serializer_class = PersonaSerializer

class RateViewSet(viewsets.ModelViewSet):
	queryset = Rate.objects.all()
	serializer_class = RateSerializer

class AutorLibroViewSet(viewsets.ModelViewSet):
	queryset = Autor_Libro.objects.all()
	serializer_class = AutorLibroSerializer
