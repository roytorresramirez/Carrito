from django.db import models

# Create your models here.

class Categoria(models.Model):
	titulo = models.CharField(max_length = 140)

	def __unicode__(self):
		return self.titulo

class Item(models.Model):
	nombre = models.CharField(max_length = 40)
	descripción = models.CharField(max_length = 70)
	precio = models.