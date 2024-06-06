from django.urls import path
from . import views

urlpatterns = [
    path('books',views.books),
    path('drf',views.getDrf),
    path('orders',views.Orders.listOrders),
    path('books/<int:pk>',views.BookView.as_view()),
    # path('booklist',views.BookList.as_view())
]