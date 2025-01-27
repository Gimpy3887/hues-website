from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('commands/', views.commands, name='commands'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
]
