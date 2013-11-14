from django.conf.urls import patterns, include, url
from .views import home

urlpatterns = patterns('',
    # Examples:
    url(r'^home/$', home.as_view()),
    
)