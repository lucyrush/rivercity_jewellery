from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Oops! There's nothing in your shopping bag yet")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HpypAFpxnBOK7a4WBfHNnmv95HUa5etMqUUGXWwCKF9xc7I33wBh5GQN73lsr791gaX9DKxXXkhgi2wIuhgCoNn001Zi4CTxu',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
