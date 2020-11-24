from django.urls import path

from . import views

urlpatterns = [
    path('accordion/', views.accordion, name = 'accordion'),
]