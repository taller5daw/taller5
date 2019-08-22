from django.shortcuts import render
from rest_framework_mongoengine import viewsets
from .serializer import *


# Create your views here.

class librosViewSet(viewsets.ModelViewSet):
	lookup_field = 'id'
	serializer_class = librosSerializer
	queryset = libros.objects.all()