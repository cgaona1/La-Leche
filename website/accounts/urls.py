from django.urls import path

from .views import SignUpView

urlpatters = [
    path('signup/', SignUpView.as_View(), name = 'signup'),
]