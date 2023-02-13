from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products:all_products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MU89QG0etn7Vxsoho7woZ7qHhsSBphjXkxoqb6NZoWfaglAF9B1U6eeYhJUo4nBSyuoS4IHdOrI2mj6gjjeUo7W00P4Q643zl',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)