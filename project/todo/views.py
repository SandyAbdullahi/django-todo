from django.shortcuts import render

def LANDING(request):
    return render(request, 'pages/landing.html')

def ABOUT(request):
    return render(request, 'pages/about.html')
