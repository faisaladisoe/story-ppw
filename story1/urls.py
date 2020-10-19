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
]