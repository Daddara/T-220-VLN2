from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from cart.models import Cart
from consoles.models import Consoles
from games.models import Games


@login_required
def add_to_cart(request, id):
    user = User.objects.filter(pk=request.user.id).first()
    if request.GET['type'] == 'game':
        g = Games.objects.filter(pk=id).first()
        cart_instance = Cart.objects.filter(u=user, game=g).first()
        if cart_instance == None:
            c = Cart(u=user, game=g, quantity=1)
            c.save()
        else:
            cart_instance.quantity += 1
            cart_instance.save()
    if request.GET['type'] == 'console':
        co = Consoles.objects.filter(pk=id).first()
        cart_instance = Cart.objects.filter(u=user, console=co).first()
        if cart_instance == None:
            c = Cart(u=user, console=co, quantity=1)
            c.save()
        else:
            cart_instance.quantity += 1
            cart_instance.save()

    return redirect('co-index')

