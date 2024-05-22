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
    """
    This view renders the home page for the fareflex app.

    It retrieves all the wallets from the database and passes them to the template.

    :param request: The HTTP request object.
    :return: An HttpResponse object.
    """
    # Get all the wallets from the database
    wallets = Wallet.objects.all()

    # Render the home template with the wallets
    return render(request, 'fareflex/home.html', {'wallets': wallets})

def about(request):
    """
    This view renders the about page for the fareflex app.

    :param request: The HTTP request object.
    :return: An HttpResponse object.
    """
    return render(request, 'fareflex/about.html')

@csrf_exempt
def create_wallet(request):
    """
    This view creates a new wallet and adds it to the database.

    It first checks if the request method is POST and if the form is valid.
    If the form is valid, it retrieves the wallet's label, currency, and can_disburse
    fields from the form, creates a new wallet using the API service, and adds it to
    the database.

    If the form is not valid, it displays an error message to the user.

    :param request: The HTTP request object.
    :return: An HttpResponse object.
    """
    current_user = request.user
    print(f"Request method: {request.method}")
    if request.method == 'POST':
        form = WalletForm(request.POST)
        print(f"Form valid: {form.is_valid()}")
        if form.is_valid():
            # Retrieve the wallet's label, currency, and can_disburse fields from the form
            label = form.cleaned_data.get('label')
            currency = form.cleaned_data.get('currency')
            can_disburse = form.cleaned_data.get('can_disburse')

            # Create a new wallet using the API service
            response = service.wallets.create(currency=currency, label=label, can_disburse=can_disburse)

            # If the API response is successful, add the wallet to the database
            if response['wallet_id']:
                wallet_id = response['wallet_id']
                try:
                    Wallet.objects.create(wallet_id=wallet_id, label=label, currency=currency, can_disburse=can_disburse, user_id=current_user.id)
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
