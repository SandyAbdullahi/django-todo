from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.LANDING, name='landing'),
    path('about/', views.ABOUT, name='about'),
    path('register/', views.NEW_USER, name='sign_up'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', views.DASHBOARD, name='dashboard'),
    path('dashboard/update_list/<int:list_id>/', views.UPDATE_LIST, name='update'),
    path('dashboard/delete_list/<int:list_id>/', views.DELETE_LIST),
    path('dashboard/update_list/<int:list_id>/delete_item/<int:item_id>/', views.DELETE_ITEM),
]
