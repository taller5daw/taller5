from django.db import models

# Create your models here.
class User(models.Model):
	email = models.CharField(max_length=40,primary_key=True)
	contrasena = models.CharField(max_length=10)

class Autor(models.Model):
	id_autor = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)

class Libro(models.Model):
	id_libro = models.AutoField(primary_key=True)
	title = models.CharField(max_length=50)
	isbn = models.CharField(max_length=50)
	mean_rate = models.DecimalField(null=True, max_digits=3, decimal_places=2)


class Persona(models.Model):
	id_persona = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	cedula = models.CharField(max_length=11)
	fecha = models.CharField(max_length=20)
	user = models.ForeignKey(User, null=False,blank=False, on_delete=models.CASCADE)


class Rate(models.Model):
	user = models.ForeignKey(User, null=False,blank=False,on_delete=models.CASCADE)
	id_libro = models.ForeignKey(Libro, null=False,blank=False,on_delete=models.CASCADE)
	rate = models.IntegerField(null=True)
	class Meta:
		unique_together=('user','id_libro')

class Autor_Libro(models.Model):
	id_autor = models.ForeignKey(Autor,null=False,blank=False,on_delete=models.CASCADE)
	id_libro = models.ForeignKey(Libro, null=False,blank=False, on_delete=models.CASCADE)
	class Meta:
		unique_together=('id_autor','id_libro')

