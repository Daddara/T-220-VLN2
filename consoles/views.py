from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from consoles.models import Consoles
# Create your views here.

def index(request):
    if 'search_filter' in request.GET:
        print("hæ")
        search_filter = request.GET['search_filter']
        consoles = [ {
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'image': x.image
        } for x in Consoles.objects.filter(name__icontains=search_filter) ]
        return JsonResponse({ 'data': consoles})
    context = {'consoles': Consoles.objects.all().order_by('name')}
    return render(request, 'consoles/index.html', context)

def get_console_by_id(request, id):
    return render(request, 'consoles/console_details.html', {
        'console': get_object_or_404(Consoles, pk=id)
    })
