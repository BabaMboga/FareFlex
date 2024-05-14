from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    user_type_choices = [
        ('passenger', 'Passenger'),
        ('driver', 'Driver'),
        ('conductor', 'Conductor'),
    ]

    username = models.CharField(max_length=150, unique=True)
    user_type = models.CharField(max_length=20, choices=user_type_choices)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=15)
    intasend_wallet_id = models.CharField(max_length=100, blank=True, null=True)

    class Wallet(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        balance = models.DecimalField(max_digits=10, decimal_places=2)
        currency = models.CharField(max_length=3)
        last_updated = models.DateTimeField(auto_now=True)

    class Transaction(models.Model):
        transaction_type_choices = [
            ('debit', 'Debit'),
            ('credit', 'Credit'),

        ]
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
        transaction_type = models.CharField(max_length=10, choices=transaction_type_choices)
        amount = models.DecimalField(max_digits=10, decimal_places=2)
        description = models.TextField()
        timestamp = models.DateTimeField(auto_now_add=True)

    class PaymentMethod(models.Model):
        payment_type_choices = [
            ('credit_card', 'Credit Card'),
            ('bank_account', 'Bank Account'),
            ('mobile_money', 'Mobile Money'),

        ]

        user = models.ForeignKey(User, on_delete=models.CASCADE)
        payment_type = models.CharField(max_length=20, choices=payment_type_choices)
        details = models.TextField()

    class Route(models.Model):
        route_name = models.CharField(max_length=100)
        start_location = models.CharField(max_length=100)
        end_location = models.CharField(max_length=100)
        distance = models.DecimalField(max_digits=10, decimal_places=2)
        price = models.DecimalField(max_digits=10, decimal_places=2)

    class Vehicle(models.Model):
        route = models.ForeignKey(Route, on_delete=models.CASCADE)
        vehicle_id = models.CharField(max_length=20, unique=True)
        driver_name = models.CharField(max_length=150)
        conductor_name = models.CharField(max_length=150)
        capacity = models.IntegerField()
        status = models.BooleanField(default=True)
