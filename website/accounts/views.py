
from django.views.generic import TemplateView, CreateView

from django.contrib.auth.forms import UserCreationForm
from .forms import NotificationForm
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = 'home.html'


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class NotificationPageView(CreateView):
    form_class = NotificationForm
    template_name = "email_notification_page.html"
