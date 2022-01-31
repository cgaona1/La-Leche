
from django.contrib import admin
from django.urls import path

from accounts.views import AccountDeleteView, AccountDetailView, AccountCreateView, AccountUpdateView, SignUpView

urlpatterns = [

    # Account Views
    path('login/',             SignUpView.as_view(),    name='login'),
    path('<int:pk>',           AccountDetailView.as_view(),  name='account_detail'),
    path('add',                AccountCreateView.as_view(),  name='account_add'),
    path('<int:pk>/',          AccountUpdateView.as_view(),  name='account_edit'),
    path('<int:pk>/delete',    AccountDeleteView.as_view(),  name='account_delete'),

    # Sign Up
    path('signup/', SignUpView.as_view(), name='signup'),
]