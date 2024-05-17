from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from intasend import APIService

TEST_API_TOKEN = "ISSecretKey_test_aea56f44-d051-4796-a075-759b2406bb19"
TEST_PUBLISHABLE_KEY = "ISPubKey_test_693bfb0f-b98c-4069-97e8-7927af92d66f"

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('fareflex-home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def pay_fare(request):
    publishable_key = "INTASEND_PUBLISHABLE_KEY"
    service = APIService(token=TEST_API_TOKEN, publishable_key=TEST_PUBLISHABLE_KEY, test=True)

    response = service.collect.checkout(phone_number=254727563415,
                                    email="mulirokhaemba@gmail.com", amount=10, currency="KES", comment="Service Fees", redirect_url="http://example.com/thank-you")
    payment_url = response.get("url")
    return render(request, 'users/pay_fare.html', {'payment_url': payment_url})

