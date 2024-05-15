from django.http import HttpResponse
from intasend import APIService
from django.shortcuts import render, redirect
from .forms import WalletForm
from .models import Wallet
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect, csrf_exempt

TEST_API_TOKEN = "ISSecretKey_test_aea56f44-d051-4796-a075-759b2406bb19"
TEST_PUBLISHABLE_KEY = "ISPubKey_test_693bfb0f-b98c-4069-97e8-7927af92d66f"
service = APIService(token=TEST_API_TOKEN, publishable_key=TEST_PUBLISHABLE_KEY, test=True)

# Create your views here.
@csrf_exempt
def home(request):
    wallets = Wallet.objects.all()
    return render(request, 'fareflex/home.html', {'wallets': wallets})

def about(request):
    return render(request, 'fareflex/about.html')

@csrf_exempt
def create_wallet(request):
    print(f"Request method: {request.method}")
    if request.method == 'POST':
        form = WalletForm(request.POST)
        print(f"Form valid: {form.is_valid()}")
        if form.is_valid():
            label = form.cleaned_data.get('label')
            currency = form.cleaned_data.get('currency')
            can_disburse = form.cleaned_data.get('can_disburse')
            response = service.wallets.create(currency=currency, label=label, can_disburse=can_disburse)
            print(response.get('status'))
            if response.get('status') == "success":
                wallet_id = response.get('data').get('id')
                try:
                    Wallet.objects.create(wallet_id=wallet_id, label=label, currency=currency, can_disburse=can_disburse)
                    messages.success(request, 'Wallet successfully created.')
                    #print(response)
                except Exception as e:
                        print(f"Error calling service.wallets.create: {e}")
                        response = None
            else:
                print(f"API response status not success: {response.get('status')}")
    else:
        form = WalletForm()
        messages.error(request, 'Failed to create wallet.')
    return render(request, 'fareflex/wallet.html', {'form': form})
