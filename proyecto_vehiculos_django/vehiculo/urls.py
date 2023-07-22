from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('vehiculo/add/', views.vehiculo_add, name='vehiculo_add'),
    path('register/', views.register_user, name='register'),
    path('vehiculo/list/', views.vehiculo_list, name='vehiculo_list'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
