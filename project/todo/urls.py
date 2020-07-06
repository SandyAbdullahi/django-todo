from django.urls import path

from . import views


urlpatterns = [
    path('', views.LANDING, name='landing'),
    path('about/', views.ABOUT, name='about'),
    path('register/', views.NEW_USER, name='sign_up'),
]
