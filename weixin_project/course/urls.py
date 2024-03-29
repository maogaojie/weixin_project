"""weixin_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path

from course import views

urlpatterns = [
    path('getcourse/', views.GetCourseAPIView.as_view()),
    path('getcoursedetail/', views.GetCourseDetail.as_view()),
    path('getstore/', views.GetStoreAPIView.as_view()),
    path('getcoach/', views.GetCoachAPIView.as_view()),
    path('getdirection/', views.GetCourseDirection.as_view()),
    path('getcoursedirection/', views.DirectionAPIView.as_view()),
    path('getprivatecourse/', views.PrivateCourse.as_view()),
    path('getpubliccourse/', views.PublicCourseAPIView.as_view()),
]
