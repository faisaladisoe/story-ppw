from django.urls import path

from . import views

urlpatterns = [
    path('events/', views.events, name = 'events'),
    path('events/addEvents/', views.addEvents, name = 'addEvents'),
    path('events/deleteEvents/<str:pk>/', views.deleteEvents, name = 'deleteEvents'),
    path('events/eventDetails/<str:pk>/', views.eventDetails, name = 'eventDetails'),
    path('events/registerVisitor/<str:pk>/', views.registerVisitor, name = 'registerVisitor'),
    path('events/updateVisitor/<str:pk>/', views.updateVisitor, name = 'updateVisitor'),
    path('events/deleteVisitor/<str:pk>/', views.deleteVisitor, name = 'deleteVisitor'),
]