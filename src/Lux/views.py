from django.shortcuts import render

from Lux.models import Category
from django.views.generic import TemplateView
# Create your views here.


class HomeView(TemplateView):
    template_name= 'home.html'

home = HomeView.as_view()

def contato(request):
    return render(request, 'contato.html')