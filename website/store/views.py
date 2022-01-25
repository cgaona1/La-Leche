
from itertools import product
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView
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


class OwnerPage(TemplateView):
    mode = Product
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
