from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def LANDING(request):
    count = User.objects.count()
    context = {
        'count': count
    }
    return render(request, 'pages/landing.html', context)

def ABOUT(request):
    return render(request, 'pages/about.html')


def NEW_USER(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing')
    else:
        form = UserCreationForm()
        context = {
            'form': form
        }
    return render(request, 'registration/sign_up.html', context)
