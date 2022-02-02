
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Store
# Create your views here.


class HomePage(TemplateView):
    model = Store
    template_name = "home.html"


class AdminPage(TemplateView):
    mode = Store
    template_name = "adminpage.html"
