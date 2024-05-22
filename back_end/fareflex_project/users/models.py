from django.db import models

class UserCustomer(models.Model):
    """
    A UserCustomer represents a customer who is using the application.
    """
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    reference = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    customer_id = models.CharField(max_length=255, default="")
    created_at = models.DateTimeField(default=None)
    updated_at = models.DateTimeField(default=None)

    def __str__(self):
        return self.email

