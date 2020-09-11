from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home.html', views.home, name='home'),
    path('platform.html', views.platform, name='platform'),
    path('customer.html', views.customer, name='customer'),
    path('team.html', views.team, name='team'),
    path('contact.html', views.contact, name='contact'),
]