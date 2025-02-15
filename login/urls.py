from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.HomeView.as_view(), name='home'),
    path('logout/', views.logout_view, name='logout'),
]