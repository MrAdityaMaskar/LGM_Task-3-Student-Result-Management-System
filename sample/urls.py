from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('result/', views.sample, name="home"),
    path('student_info/', views.student, name="home"),
]





