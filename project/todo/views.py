
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import ListForm


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
            form.clean()
            return redirect('login')
    else:
        form = UserCreationForm()
        context = {
            'form': form
        }
    return render(request, 'registration/sign_up.html', context)


@login_required
def DASHBOARD(request):
    user = request.user
    user_id = user.id
    if request.method == 'POST':
        new_list_form = ListForm(request.POST)
        if new_list_form.is_valid():
            new_list_form.save()
            new_list_form.clean()
            return redirect('dashboard')
    else:
        new_list_form = ListForm(initial={"user":user_id})

    context = {
        'form': new_list_form
    }
    return render(request, 'pages/dashboard.html', context)