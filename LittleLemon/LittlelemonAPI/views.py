from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MenuItem
from .serializers import MenuItemSerializer
from django.shortcuts import get_object_or_404

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


# view function to list all menu items
@api_view(['GET'])
def menu_items(request):
    menu_items = MenuItem.objects.all()
    serializer = MenuItemSerializer(menu_items, many=True)
    return Response(serializer.data)
    # return Response(menu_items.values())

@api_view(['GET'])
def single_item (request, pk):
    # menu_item = MenuItem.objects.get(pk=pk)
    menu_item = get_object_or_404(MenuItem, pk=pk)
    serializer = MenuItemSerializer(menu_item)
    return Response(serializer.data)