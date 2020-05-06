from django.shortcuts import render, get_object_or_404
from games.models import Games


# Create your views here.

def index(request):
    context = {'games': Games.objects.all().order_by('name')}
    return render(request, 'games/index.html', context)


def get_game_by_id(request, id):
    return render(request, 'games/game_details.html', {
        'game': get_object_or_404(Games, pk=id)
    })
