from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Wallet(models.Model):
    wallet_id = models.CharField(max_length=255, default=1)
    label = models.CharField(max_length=255, default="payment")
    currency = models.CharField(max_length=3)
    can_disburse = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.wallet_id
    
class Route(models.Model):
    id = models.AutoField(primary_key=True)
    route_name = models.CharField(max_length=255, default="ma3-routes")
    start_location = models.CharField(max_length=255, default="payment")
    stop_location = models.CharField(max_length=255, default="payment")
    distance = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    
    def __str__(self):
        return self.route_name

class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    route_id = models.ForeignKey(Route, on_delete=models.CASCADE)
    vehicle_number = models.CharField(max_length=20, default="payment")
    driver_name = models.CharField(max_length=50, default="payment")
    conductor_name = models.CharField(max_length=50, default="payment")
    capacity = models.IntegerField(default=14)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.vehicle_number

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    wallet_id = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=255, default="payment")
    amount = models.IntegerField(default=0)
    timestamp = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=255, default="payment")
    
    def __str__(self):
        return self.transaction_type

class PaymentMethod(models.Model):
    id = models.AutoField(primary_key=True)
    payment_type = models.CharField(max_length=255, default="payment")
    details = models.CharField(max_length=255, default="payment")
    
    def __str__(self):
        return self.payment_type
