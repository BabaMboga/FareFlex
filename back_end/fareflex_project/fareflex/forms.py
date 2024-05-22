from django import forms
from .models import Wallet

class WalletForm(forms.ModelForm):
    """
    A form for creating a new wallet.
    """
    class Meta:
        """
        Meta class for WalletForm.
        """
        model = Wallet
        fields = ['label', 'currency', 'can_disburse']
