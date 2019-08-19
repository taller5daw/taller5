from django.db import models

# Create your models here.

class Book(Document):
	title = fields.StringField()
	authors = fields.StringField()
	isbn = fields.StringField()
	rate = fields.StringField()


