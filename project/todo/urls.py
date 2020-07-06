from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.LANDING, name='landing'),
    path('about/', views.ABOUT, name='about'),
    path('register/', views.NEW_USER, name='sign_up'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', views.DASHBOARD, name='dashboard'),
]
