import string
from random import choice

from django.db import models

# Create your models here.

class UserRegistered(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    token = models.CharField(max_length=6)

    def __unicode__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.pk:
            self.token = self.get_token()

            while(UserRegistered.objects.filter(token=self.token).exists()):
                self.token = self.get_token()

        super(UserRegistered, self).save(*args, **kwargs)

    def get_token(self):
        chars = string.ascii_letters + string.digits
        token = ''.join(choice(chars) for i in range(6))

        return token

class Categoria(models.Model):
	nombre = models.CharField(max_length = 140)

	def __unicode__(self):
		return self.nombre

class Item(models.Model):
	titulo = models.CharField(max_length = 140)
	descripcion = models.TextField()
	precio = models.DecimalField()
	categoria = models.ForeignKey(Categoria)
	imagen = models.ImageField(upload_to='catalogo')

	def __unicode__():
		return self.titulo
class Mail(models.Model):
	subject = models.CharField(max_length = 255)
	to = models.CharField(max_length = 255)
	from_email = models.EmailField()
	template = models.CharField(max_length=255)
    data = models.TextField()
    sent = models.BooleanField(default=False, blank=True)
    date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, blank=True)
    reject_reason = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.to
