from django.shortcuts import render

# Create your views here.
from cart.models import Cart


def index(request):
    context = {'cart': Cart.objects.all().order_by('game')}
    return render(request, 'checkout/checkout.html', context)