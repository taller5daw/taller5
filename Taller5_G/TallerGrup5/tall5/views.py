from django.shortcuts import render
from rest_framework_mongoengine import viewsets
from .serializer import librosSerializer
from .models import libros

# Create your views here.

class librosViewSet(viewsets.ModelViewSet):
	lookup_field = 'id'
	queryset = libros.objects.all()
	serializer_class = librosSerializer