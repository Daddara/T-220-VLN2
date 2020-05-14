from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from games.forms.game_form import GameCreateForm, GameUpdateForm
from games.models import Games


# Create your views here.

def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        games = [ {
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'image': x.image,
            'price': x.price
        } for x in Games.objects.filter(name__icontains=search_filter) ]
        return JsonResponse({ 'data': games })
    def_order = 'name'

    if 'sort' in request.GET:
        sort = request.GET['sort']
        def_order = sort

    if 'consoles' in request.GET:
        consoles = request.GET['consoles']
        games = [ {
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'image': x.image,
            'price': x.price
        } for x in Games.objects.filter(console_id=consoles) ]
        return JsonResponse({ 'data': games })

    context = {'games': Games.objects.all().order_by(def_order) }
    return render(request, 'games/index.html', context)


def get_game_by_id(request, id):
    return render(request, 'games/game_details.html', {
        'game': get_object_or_404(Games, pk=id)
    })


def create_game(request):
    if request.method == "POST":
        form = GameCreateForm(data=request.POST)
        if form.is_valid():
            game = form.save()
            return redirect('games-index')
    else:
        form = GameCreateForm()
    return render(request, 'games/create_game.html', {
        'form': form
    })


def delete_game(request, id):
    game = get_object_or_404(Games, pk=id)
    game.delete()
    return redirect('games-index')


def update_game(request, id):
    instance = get_object_or_404(Games, pk=id)
    if request.method == "POST":
        form = GameUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('games_details', id=id)
    else:
        form = GameUpdateForm(instance=instance)
    return render(request, 'games/update_game.html', {
        'form': form,
        'id': id
    })


