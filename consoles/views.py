from django.shortcuts import render, get_object_or_404

from consoles.models import Consoles
# Create your views here.

def index(request):
    context = {'consoles': Consoles.objects.all().order_by('name')}
    return render(request, 'consoles/index.html', context)

def get_console_by_id(request, id):
    return render(request, 'consoles/console_details.html', {
        'console': get_object_or_404(Consoles, pk=id)
    })
