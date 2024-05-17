from django import forms
from .models import UserCustomer

class UserCustomerForm(forms.ModelForm):
    class Meta:
        model = UserCustomer
        fields = ['email', 'first_name', 'last_name', 'reference', 'address', 'city', 'state', 'zipcode', 'country']