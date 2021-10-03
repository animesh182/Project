from django.shortcuts import render
from django.http import HttpResponse

from lending_system.settings import TEMPLATES
from .models import Products
from django.shortcuts import render
from django.views.generic import TemplateView

def index(request):
    prods=Products.objects.all()
    return render(request, 'homepage/index.html',{'products':prods})


class HomePageView(TemplateView):
    template_name='index.html'

    
