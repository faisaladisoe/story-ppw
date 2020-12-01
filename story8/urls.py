from django.urls import path

from . import views

urlpatterns = [
    path('bookCollection/', views.bookCollection, name = 'bookCollection'),
]