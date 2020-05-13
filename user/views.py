from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from user.models import Profile


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': UserCreationForm()
        })

def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        print(1)
    return render(request, 'user/profile.html', {
        'form': ''
    })