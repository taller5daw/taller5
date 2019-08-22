from django.db import models
from mongoengine import Document,EmbeddedDocument, fields


# Create your models here.

class libros(Document):
	titulo = fields.StringField()
	autores = fields.StringField()
	isbn = fields.StringField()
	calificacionprom = fields.StringField()


