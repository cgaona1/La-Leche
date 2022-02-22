

from itertools import product
from socket import herror
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from tempfile import template
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from .models import Product
# Create your views here.

# this is a test
# sdbsbhhsbs


class HomePage(ListView):
    model = Product
    template_name = "home.html"

    # def get_products(request):
    #     product_list = Product.objects.all()
    #     return render(request, '../template/home.html', {'product_list': product_list})

    # def get_context_data(self, **kwargs):

    #     product = Product.objects.all()
    #     return{'product': product}


class OwnerPage(ListView):
    model = Product
    template_name = "ownerPage.html"


class CreateItem(CreateView):
    model = Product
    template_name = "add_item.html"
    fields = ['name', 'cost', 'quantity', 'image']
    success_url = reverse_lazy('home')


class DeletePage(TemplateView):
    model = Product
    template_name = "delete_item.html"
    success_url = reverse_lazy('home')


class Contact_Info(TemplateView):
    model = Product
    template_name = "contact_page.html"

class NotificationPage(TemplateView):
    template_name = "email_notification_page.html"

class Detail_View(TemplateView):
    model = Product
    template_name = "item_detail.html"

    def get_context_data(self, **kwargs):
        product_id = kwargs['pk']
        product = Product.objects.get(pk=product_id)
        return {'product': product}

class SignUpView(generic.CreateView):
    model= Product
    template_name= 'registration/login.html'
