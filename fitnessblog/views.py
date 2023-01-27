from django.shortcuts import render, redirect
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def donation(request):
    key = settings.STRIPE_PUBLISHABLE_KEY
    if request.method == "POST":
        # Get the payment token from the form
        token = request.POST.get("stripeToken")
        amount = request.POST.get("amount")

        # Create the charge on Stripe's servers
        try:
            charge = stripe.Charge.create(
                amount=int(amount) * 100,  # convert amount to cents
                currency="usd",
                source=token,
                description="Example donation"
            )
            # Handle successful charge
            return redirect("success")
        except stripe.error.CardError as e:
            # Handle card errors
            return redirect("error")

    # Render the payment form if the request is a GET request
    return render(request, "donation.html", {"key": key})



def success(request):
    return render(request, "success.html")

def error(request):
    return render(request, "error.html")




