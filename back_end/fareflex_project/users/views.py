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
    service = APIService(token=TEST_API_TOKEN, publishable_key=TEST_PUBLISHABLE_KEY, test=True)
    customer_response_data = None
    # Define the URL for the API endpoint
    url = "https://sandbox.intasend.com/api/v1/subscriptions-customers/"
    
    # Define the headers for the API request
    headers = {
        # Specify the format of the API response
        "accept": "application/json",
        # Specify the format of the API request
        "content-type": "application/json",
        # Include the authentication token in the request headers
        "Authorization": "Bearer ISSecretKey_test_aea56f44-d051-4796-a075-759b2406bb19"
    }

    print(f"Request method: {request.method}")

    # Check if the request method is POST
    if request.method == 'POST':
        # Create an instance of the UserCustomerForm class with the data from the request
        
        
        # Check if the form is valid
        
            # Concatenate the first and last names to create a unique username
        username = request.cleaned_data.get('first_name') + request.cleaned_data.get('last_name')
            
        print(f"Form data: {request.cleaned_data}")
            
            # Create a dictionary containing the customer data
        customer_data = {
                "email": request.cleaned_data.get('email'),
                "first_name": request.cleaned_data.get('first_name'),
                "last_name": request.cleaned_data.get('last_name'),
                "reference": request.cleaned_data.get('reference'),
                "address": request.cleaned_data.get('address'),
                "city": request.cleaned_data.get('city'),
                "state": request.cleaned_data.get('state'),
                "zipcode": request.cleaned_data.get('zipcode'),
                "country": request.cleaned_data.get('country')
            }
            
        print(f"Customer data: {customer_data}")
            
            # Send a POST request to the API endpoint with the customer data
        customer_response = request.post(url, json=customer_data, headers=headers)
            
        print(f"Customer response: {customer_response.text}")
            
            # Parse the JSON response from the API
        customer_response_data = customer_response.json()
            
        print(f"Customer response data: {customer_response_data}")
            
            # Check if the API response contains a customer_id
    if customer_response_data['customer_id']:
                # Create a new user in the database using the response data
        customer = UserCustomer.objects.create(**customer_response_data)
        customer.save()
                
                # Display a success message to the user
        messages.success(request, f'Account created for {username}!')
                
                # Redirect the user to the fareflex-home page
        return customer_response_data
    else:
                # Display an error message to the user
            messages.error(request, f"Failed to create account: {customer_response_data.get('message')}")

    
    # Render the register.html template with the form data
    # return render(request, 'users/register.html', {'form': form})
    print(f"Customer response data: {customer_response_data}")
    return customer_response_data

def pay_fare(request):
    service = APIService(token=TEST_API_TOKEN, publishable_key=TEST_PUBLISHABLE_KEY, test=True)
    response = service.collect.checkout(phone_number=254727563415,
                                        email="mulirokhaemba@gmail.com", amount=10, currency="KES",
                                        comment="Service Fees", redirect_url="http://example.com/thank-you")
    return render(request, 'users/pay_fare.html', {'payment_url': response.get('url', '')})

