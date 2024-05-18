from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Wallet(models.Model):
    wallet_id = models.CharField(max_length=255, default=1)
    label = models.CharField(max_length=255, default="payment")
    currency = models.CharField(max_length=3)
    can_disburse = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    """
    Return a string representation of the Wallet object.
    
    This string representation will be used in the admin interface
    and in the API responses.
    
    Returns:
        str: The string representation of the Wallet object.
    """
    def __str__(self):
        return self.wallet_id
    
class Route(models.Model):
    """
    A Route represents a route that a vehicle travels on.
    
    Attributes:
        id (int): The primary key of the Route object.
        route_name (str): The name of the route.
        start_location (str): The starting location of the route.
        stop_location (str): The stopping location of the route.
        distance (int): The distance of the route.
        price (int): The price of the route.
    """
    id = models.AutoField(primary_key=True)
    route_name = models.CharField(max_length=255, default="ma3-routes")
    start_location = models.CharField(max_length=255, default="payment")
    stop_location = models.CharField(max_length=255, default="payment")
    distance = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    
    def __str__(self):
        """
        Return a string representation of the Route object.
        
        This string representation will be used in the admin interface
        and in the API responses.
        
        Returns:
            str: The string representation of the Route object.
        """
        return self.route_name

class Vehicle(models.Model):
    """
    A Vehicle represents a vehicle that travels on a route.
    
    Attributes:
        id (int): The primary key of the Vehicle object.
        route_id (Route): The route that the vehicle travels on.
        vehicle_number (str): The number of the vehicle.
        driver_name (str): The name of the driver.
        conductor_name (str): The name of the conductor.
        capacity (int): The capacity of the vehicle.
        status (bool): The status of the vehicle.
    """
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
    """
    A Transaction represents a transaction that a user makes using a wallet.
    
    Attributes:
        id (int): The primary key of the Transaction object.
        user_id (User): The user who made the transaction.
        wallet_id (Wallet): The wallet used for the transaction.
        transaction_type (str): The type of the transaction.
        amount (int): The amount of the transaction.
        timestamp (datetime): The timestamp of the transaction.
        description (str): The description of the transaction.
    """
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
    """
    A PaymentMethod represents a payment method that a user can use to make a transaction.
    
    Attributes:
        id (int): The primary key of the PaymentMethod object.
        payment_type (str): The type of the payment method.
        details (str): The details of the payment method.
    """
    id = models.AutoField(primary_key=True)
    payment_type = models.CharField(max_length=255, default="payment")
    details = models.CharField(max_length=255, default="payment")
    
    def __str__(self):
        return self.payment_type
