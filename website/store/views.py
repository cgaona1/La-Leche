

from socket import herror
from tempfile import template
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from .models import Product
from django.shortcuts import render
# Create your views here.


def search_item(request):
    print(request.GET)
    query_dict = request.GET
    query = query_dict.get('q')
    product_obj = None
    if query is not None:
        product_obj = Product.objects.get(id=query)
    context = {
        "product": product_obj
    }

    return render(request, "../template/search.html", context=context)


class HomePage(ListView):
    model = Product
    template_name = "home.html"


class OwnerPage(ListView):
    model = Product
    template_name = "ownerPage.html"

    # def get_context_data(self, **kwargs):
    #     product_id = kwargs['pk']
    #     product = Product.objects.get(pk=product_id)
    #     return {'product': product}


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
