from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from intasend import APIService
from .models import UserCustomer
from .forms import UserCustomerForm
import requests

TEST_API_TOKEN = ""
TEST_PUBLISHABLE_KEY = ""

# Create your views here.
def register(request):
    # Create an instance of the APIService class
    service = APIService(token=TEST_API_TOKEN, publishable_key=TEST_PUBLISHABLE_KEY, test=True)
    
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

    # Check if the request method is POST
    if request.method == 'POST':
        # Create an instance of the UserCustomerForm class with the data from the request
        form = UserCustomerForm(request.POST)
        
        # Check if the form is valid
        if form.is_valid():
            # Concatenate the first and last names to create a unique username
            username = form.cleaned_data.get('first_name') + form.cleaned_data.get('last_name')
            
            # Create a dictionary containing the customer data
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
            
            # Send a POST request to the API endpoint with the customer data
            customer_response = requests.post(url, json=customer_data, headers=headers)
            
            # Parse the JSON response from the API
            customer_response_data = customer_response.json()
            
            # Check if the API response contains a customer_id
            if customer_response_data['customer_id']:
                # Create a new user in the database using the response data
                customer = UserCustomer.objects.create(**customer_response_data)
                customer.save()
                
                # Display a success message to the user
                messages.success(request, f'Account created for {username}!')
                
                # Redirect the user to the fareflex-home page
                return redirect('fareflex-home')
            else:
                # Display an error message to the user
                messages.error(request, f"Failed to create account: {customer_response_data.get('message')}")
    else:
        # If the request method is not POST, create an instance of the UserCreationForm class
        form = UserCreationForm()
    
    # Render the register.html template with the form data
    return render(request, 'users/register.html', {'form': form})

def pay_fare(request):
    service = APIService(token=TEST_API_TOKEN, publishable_key=TEST_PUBLISHABLE_KEY, test=True)
    response = service.collect.checkout(phone_number=254727563415,
                                        email="mulirokhaemba@gmail.com", amount=10, currency="KES",
                                        comment="Service Fees", redirect_url="http://example.com/thank-you")
    return render(request, 'users/pay_fare.html', {'payment_url': response.get('url', '')})

