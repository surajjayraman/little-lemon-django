from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('datetime/', views.display_datetime, name = 'datetime'),
]