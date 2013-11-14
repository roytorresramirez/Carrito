from django.conf.urls import patterns, include, url
"""
	.views --> se coloca . para que busque en la misma carpeta
"""
from .views import catalogo


urlpatterns = patterns('',
    # Examples:
    url(r'^catalogo/$', catalogo.as_view() ),

)