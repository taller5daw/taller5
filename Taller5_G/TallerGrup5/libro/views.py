from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


from django.shortcuts import render,redirect,get_object_or_404

from .models import *

# def hello_world(request):
# 	#"Ejemplo de view"
# 	return HttpResponse("Hello world!")


# def list_autores(request):
# 	autores = Autor.objects.all().order_by('name')
# 	context = {

# 		'autores': autores
# 	}

# 	return render(request,'autores/sesion.html',context)