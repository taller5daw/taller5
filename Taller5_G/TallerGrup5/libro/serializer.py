from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'

class AutorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Autor
		fields = '__all__'

class LibroSerializer(serializers.ModelSerializer):
	class Meta:
		model = Libro
		fields = '__all__'

class PersonaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Persona
		fields = '__all__'

class RateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rate
		fields = '__all__'

class AutorLibroSerializer(serializers.ModelSerializer):
	class Meta:
		model = Autor_Libro
		fields = '__all__'

