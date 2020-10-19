from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('copyright/', views.copyright, name='copyright'),
    path('intro/', views.intro, name='introduction'),
    path('prototype/', views.prototype, name='prototype'),
    path('init-design/', views.initialDesign, name='initialDesign'),
    path('copyright-init/', views.copyrightInit, name='copyrightInit'),
    path('courseRegister/', views.courseRegister, name='courseRegister'),
    path('courseRegister/courseList/', views.courseList, name = 'courseList'),
    path('courseRegister/courseUpdate/<str:pk>/', views.courseUpdate, name = 'courseUpdate'),
    path('courseRegister/courseDelete/<str:pk>/', views.courseDelete, name = 'courseDelete'),
    path('courseRegister/courseList/<str:course_name>/', views.courseDetails, name = 'courseDetails'),
    # path('events/', views.events, name = 'events'),
    # path('events/addEvents/', views.addEvents, name = 'addEvents'),
    # path('events/deleteEvents/<str:pk>/', views.deleteEvents, name = 'deleteEvents'),
    # path('events/eventDetails/<str:pk>/', views.eventDetails, name = 'eventDetails'),
    # path('events/registerVisitor/<str:pk>/', views.registerVisitor, name = 'registerVisitor'),
]