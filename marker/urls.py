from django.urls import path
from . import views


urlpatterns = [
    path('', views.photo_list, name='photo_list'),
    path('singup/', views.singup, name='singup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
