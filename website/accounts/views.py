from re import template
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from .forms import NotificationForm
from django.urls import reverse_lazy
from django.views import generic

class HomeView(TemplateView):
    template_name = 'home.html'

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/login.html'

class NotificationPageView(CreateView):
    form_class = NotificationForm
    template_name = "email_notification_page.html"
