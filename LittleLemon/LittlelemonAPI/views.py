from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import MenuItem, Category
from .serializers import MenuItemSerializer, CategorySerializer
from django.shortcuts import get_object_or_404

# view function to list all menu items
@api_view(['GET', 'POST'])
def menu_items(request):
    if request.method == 'GET':
        menu_items = MenuItem.objects.select_related('category').all()
        serializer = MenuItemSerializer(menu_items, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = MenuItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


           

@api_view()
def single_item (request, pk):
    # menu_item = MenuItem.objects.get(pk=pk)
    menu_item = get_object_or_404(MenuItem, pk=pk)
    serializer = MenuItemSerializer(menu_item)
    return Response(serializer.data)

# view function to list all categories
@api_view()
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.select_related('category').all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.select_related('category').all()
    serializer_class = MenuItemSerializer


    # return Response(menu_items.values())
