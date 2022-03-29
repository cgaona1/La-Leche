
from django.views.generic import TemplateView, CreateView, FormView

from .forms import NotificationForm
from .services import send_email_task

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = 'home.html'


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class NotificationPageView(FormView):
    form_class = NotificationForm
    template_name = "email_notification_page.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        self.send_email(form.cleaned_data)

        return super().form_valid(form)

    def send_email(self, valid_data):
        email = valid_data['email']
        subject = valid_data['subject']
        message = valid_data['message']
        send_email_task(email, subject, message)
