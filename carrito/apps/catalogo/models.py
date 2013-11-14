from django.db import models

# Create your models here.

class Categoria(models.Model):
	titulo = models.CharField(max_length = 140)

	def __unicode__(self):
		return self.titulo

class Item(models.Model):
	titulo = models.CharField(max_length = 140)
	descripcion = models.TextField()
	#foto = models.ImageField(upload_to = 'images')

	def __unicode__(self):
		return self.titulo
