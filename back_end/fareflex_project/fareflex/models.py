from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Wallet(models.Model):
    intasend_id = models.CharField(max_length=10)
    currency = models.CharField(max_length=5)
    last_updated = models.DateTimeField(default=timezone.now)
    balance = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.intasend_id