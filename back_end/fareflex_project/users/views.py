from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from intasend import APIService
from .models import UserCustomer
from .forms import UserCustomerForm
import requests

TEST_API_TOKEN = "ISSecretKey_test_aea56f44-d051-4796-a075-759b2406bb19"
TEST_PUBLISHABLE_KEY = "ISPubKey_test_693bfb0f-b98c-4069-97e8-7927af92d66f"

# Create your views here.
def register(request):
    service = APIService(token=TEST_API_TOKEN, publishable_key=TEST_PUBLISHABLE_KEY, test=True)
    url = "https://sandbox.intasend.com/api/v1/subscriptions-customers/"
    headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "Bearer ISSecretKey_test_aea56f44-d051-4796-a075-759b2406bb19"
}

    if request.method == 'POST':
        form = UserCustomerForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('first_name') + form.cleaned_data.get('last_name')
            customer_data = {
                "email": form.cleaned_data.get('email'),
                "first_name": form.cleaned_data.get('first_name'),
                "last_name": form.cleaned_data.get('last_name'),
                "reference": username,
                "address": form.cleaned_data.get('address'),
                "city": form.cleaned_data.get('city'),
                "state": form.cleaned_data.get('state'),
                "zipcode": form.cleaned_data.get('zipcode'),
                "country": form.cleaned_data.get('country')
            }
            customer_response = requests.post(url, json=customer_data, headers=headers)
            customer_response_data = customer_response.json()
            
            # Create a new user in the database using the response data
            if customer_response_data['customer_id']:
                customer = UserCustomer.objects.create(**customer_response_data)
                customer.save()
                messages.success(request, f'Account created for {username}!')
                return redirect('fareflex-home')
            else:
                messages.error(request, f"Failed to create account: {customer_response_data.get('message')}")
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def pay_fare(request):
    publishable_key = "INTASEND_PUBLISHABLE_KEY"
    service = APIService(token=TEST_API_TOKEN, publishable_key=TEST_PUBLISHABLE_KEY, test=True)

    response = service.collect.checkout(phone_number=254727563415,
                                    email="mulirokhaemba@gmail.com", amount=10, currency="KES", comment="Service Fees", redirect_url="http://example.com/thank-you")
    payment_url = response.get("url")
    print(response)
    return render(request, 'users/pay_fare.html', {'payment_url': payment_url})

