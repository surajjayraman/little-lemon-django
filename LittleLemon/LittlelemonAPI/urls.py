from django.urls import path
from . import views

urlpatterns = [
    path('menu-items', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('menuitems', views.menu_items),
    path('menuitems/<int:pk>', views.single_item),
    path('categories/<int:pk>', views.category_detail),
]