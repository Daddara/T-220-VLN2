from django.shortcuts import render

# Create your views here.
from cart.models import Cart
from consoles.models import Consoles
from games.models import Games
from payment.models import Payment


def index(request):
    cart_instances = Cart.objects.filter(u=request.user)
    product_list = []
    price = 0
    for instance in cart_instances:
        if instance.game != None:
            game = Games.objects.filter(pk=instance.game.id).first()
            product_list.append(game)
            price += game.price
        else:
            console = Consoles.objects.filter(pk=instance.console.id).first()
            product_list.append(console)
            price += console.price
    price = round(price, 2)
    context = {'cart': product_list, 'total_price': price}
    return render(request, 'checkout/payment.html', context)


