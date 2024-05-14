from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Wallet(models.Model):
    wallet_id = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    currency = models.CharField(max_length=3)
    can_disburse = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.intasend_id