from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='fareflex-home'),
    path('about/', views.about, name='fareflex-about'),
    path('wallet/', views.create_wallet, name='fareflex-wallet')
]