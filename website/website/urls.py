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

from django.contrib import admin
from django.urls import path, include
from store.views import *
from accounts.views import *
from django.conf import settings
from django.conf.urls.static import static

# wesite urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('search', search_item, name="search"),
    path('', HomePage.as_view(), name="home"),
    path('add', CreateItem.as_view(), name="add_item"),
    path('ownerpage/delete/<int:pk>/', DeletePage.as_view(), name="delete"),
    path('contact', Contact_Info.as_view(), name="contact"),
    path('notification', NotificationPageView.as_view(), name="notification"),

    path('ownerpage', OwnerPage.as_view(), name="owner"),
    path('ownerpage/<int:pk>', Update_View.as_view(), name="update"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
