import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from intasend import APIService
from .models import UserCustomer
from .forms import UserCustomerForm
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import requests

TEST_API_TOKEN = "ISSecretKey_test_aea56f44-d051-4796-a075-759b2406bb19"
TEST_PUBLISHABLE_KEY = "ISPubKey_test_693bfb0f-b98c-4069-97e8-7927af92d66f"

# Create your views here.
@csrf_exempt
def register(request):
    # Create an instance of the APIService class
    customer_response_data = {}
    service = APIService(token=TEST_API_TOKEN, publishable_key=TEST_PUBLISHABLE_KEY, test=True)
    # Define the URL for the API endpoint
    url = "https://sandbox.intasend.com/api/v1/subscriptions-customers/"
    
    # Define the headers for the API request
    headers = {
        'Access-Control-Allow-Origin': '*',
        # Specify the format of the API response
        "accept": "application/json",
        # Specify the format of the API request
        "content-type": "application/json",
        # Include the authentication token in the request headers
        "Authorization": "Bearer ISSecretKey_test_aea56f44-d051-4796-a075-759b2406bb19"
    }

    print(f"Request method: {request.method.upper()}")
    if request.body:
        data = json.loads(request.body.decode('utf-8'))
        print(f"Data: {data}")
    else:
        data = {}
            
            # Send a POST request to the API endpoint with the customer data
    customer_data = {
        "first_name": data.get('first_name'),
        "last_name": data.get('last_name'),
        "email": data.get('email'),
        "password": data.get('password'),
        "reference": data.get('reference'),
        "address": data.get('address'),
        "city": data.get('city'),
        "state": data.get('state'),
        "zipcode": data.get('zipcode'),
        "country": data.get('country'),
    }
    
    customer_response = requests.post(url, data=json.dumps(customer_data), headers=headers)
    print(f"Customer response: {customer_response}")
            
            # Parse the JSON response from the API
    customer_response_data = customer_response.json()
    customer = UserCustomer.objects.create(**customer_response_data)
    customer.save()
            
    print(f"Customer response data: {customer_response_data}")
            
            # Check if the API response contains a customer_id
    if customer_response_data.get('customer_id'):
        messages.success(request, f'Account created for')
                # Redirect the user to the fareflex-home pag
    else:
                # Display an error message to the user
        messages.error(request, f"Failed to create account: {customer_response_data.get('message')}")

    
    # Render the register.html template with the form data
    # return render(request, 'users/register.html', {'form': form})
    print(f"Customer response data: {customer_response_data}")
    return JsonResponse(customer_response_data)

def pay_fare(request):
    service = APIService(token=TEST_API_TOKEN, publishable_key=TEST_PUBLISHABLE_KEY, test=True)
    response = service.collect.checkout(phone_number=254727563415,
                                        email="mulirokhaemba@gmail.com", amount=10, currency="KES",
                                        comment="Service Fees", redirect_url="http://example.com/thank-you")
    return render(request, 'users/pay_fare.html', {'payment_url': response.get('url', '')})

