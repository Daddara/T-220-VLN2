from django.shortcuts import render

# Create your views here.
from cart.models import Cart
from consoles.models import Consoles
from games.models import Games


def index(request):
    cart_instances = Cart.objects.filter(u=request.user)
    product_list = []
    cart_ids = []
    price = 0
    for instance in cart_instances:
        if instance.game != None:
            game = Games.objects.filter(pk=instance.game.id).first()
            product_list.append(game)
            cart_ids.append(instance.id)
            price += game.price
        else:
            console = Consoles.objects.filter(pk=instance.console.id).first()
            product_list.append(console)
            cart_ids.append(instance.id)
            price += console.price
    context = {'cart': product_list, 'total_price': price, 'cart_id': cart_ids}
    return render(request, 'checkout/checkout.html', context)