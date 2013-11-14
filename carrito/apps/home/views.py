# Create your views here.
from django.views.generic import TemplateView

class home(TemplateView):
	template_name = 'home/index.html'