"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from sys import getprofile
from django.contrib import admin
from django.urls import path
from store.views import HomePage, OwnerPage, CreateItem, DeletePage, Contact_Info


# wesite urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name="home"),
    path('add', CreateItem.as_view(), name="add_item"),
    path('delete/<int:pk>', DeletePage.as_view()),
    path('contact', Contact_Info.as_view(), name="contact"),
]
