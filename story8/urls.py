from django.urls import path

from . import views

urlpatterns = [
    path('jsonResult/', views.jsonResult, name = 'json result'),
    path('bookCollection/', views.bookCollection, name = 'bookCollection'),
]