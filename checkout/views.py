from django.shortcuts import render

# Create your views here.
from cart.models import Cart
from consoles.models import Consoles
from games.models import Games


def index(request):
    cart_instances = Cart.objects.filter(u=request.user)
    product_list = []
    for instance in cart_instances:
        if instance.game != None:
            game = Games.objects.filter(pk=instance.game.id).first()
            product_list.append(game)
        else:
            console = Consoles.objects.filter(pk=instance.console.id).first()
            product_list.append(console)

    context = {'cart': product_list}
    return render(request, 'checkout/checkout.html', context)