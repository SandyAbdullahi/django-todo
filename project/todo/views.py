from django.shortcuts import render
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
    form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'registration/sign_up.html', context)
