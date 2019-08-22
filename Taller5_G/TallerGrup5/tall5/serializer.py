from rest_framework_mongoengine import serializers
from .models import libros

class librosSerializer(serializers.DocumentSerializer):
	class Meta:
		model = libros
		fields = '__all__'