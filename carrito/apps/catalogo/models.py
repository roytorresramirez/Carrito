from django.db import models

# Create your models here.

class Categoria(models.Model):
	titulo = models.CharField(max_length = 140, unique = True)

	def __unicode__(self):
		return self.titulo


class Item(models.Model):
	titulo = models.CharField(max_length = 140, unique = True)
	descripcion = models.TextField()
	contenxt = models.CharField(max_length =100)
	foto = models.ImageField(upload_to = 'images')
	slug = models.SlugField(max_length=100, blank = True)

	def save(self, *args, **kwargs):
		self.slug = self.titulo.lower().replace(" ","-")
		super(Item, self).save(*args,**kwargs)

	def __unicode__(self):
		return self.titulo