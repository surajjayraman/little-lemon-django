from django.urls import path
from . import views

urlpatterns = [
    path('books',views.books),
    path('drf',views.getDrf),
    path('orders',views.Orders.listOrders),
    path('toronto',views.getOpenData),
    # path('books/<int:pk>',views.BookView.as_view()),
    path('booklist',views.BookList.as_view()),
    path('books/<int:pk>',views.Book.as_view()),
    path('books/drf',views.BookViewAll.as_view()),
    path('books/drf/<int:pk>',views.SingleBookView.as_view()),

]