from django.urls import path
from . import views

urlpatterns = [
    path('pay_fare/', views.pay_fare, name='pay_fare'),
]
