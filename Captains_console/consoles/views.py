from django.shortcuts import render

from consoles.models import Consoles
# Create your views here.

def index(request):
    context = {'consoles': Consoles.objects.all().order_by('name')}
    return render(request, 'consoles/index.html', context)