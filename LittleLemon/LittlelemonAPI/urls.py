from django.urls import path
from . import views

urlpatterns = [
    path('menu_items/', views.MenuItemsView.as_view(), name='menu_items'),
]