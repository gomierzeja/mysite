from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('image/', views.image, name='image'),
    path('profile/', views.profile, name='profile'),
    path('contact/', views.contact, name='contact'),



]

