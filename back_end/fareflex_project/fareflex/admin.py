from django.contrib import admin
# Register your models here.


from .models import Wallet, Route, Vehicle, Transaction, PaymentMethod

admin.site.register(Wallet)
admin.site.register(Route)
admin.site.register(Vehicle)
admin.site.register(Transaction)
admin.site.register(PaymentMethod)
