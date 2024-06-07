from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import requests

# Rest framework DRF imports
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView


# Create your views here.
@csrf_exempt
def books(request):
    if request.method == 'GET':
        books = Book.objects.all().values()
        return JsonResponse({"books":list(books)})
        # return JsonResponse({"books":'list of books'})

    elif request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        book = Book(
            title = title,
            author = author,
            price = price
        )
        try:
            book.save()
        except IntegrityError:
            return JsonResponse({'error':'true','message':'required field missing'},status=400)

        return JsonResponse(model_to_dict(book), status=201)

@api_view(['GET','POST'])
def getDrf(request):
    return Response ('List of books from DRF', status=status.HTTP_200_OK)

# Different types of routing examples
class Orders():
    @staticmethod
    @api_view()
    def listOrders(request):
         return Response({'message':'list of orders'}, 200)

# Mapping class that extends the APIView
class BookView(APIView):
    def get(self, request, pk):
         return Response({"message":"single book with id " + str(pk)}, status.HTTP_200_OK)

    def put(self, request, pk):
        return Response({"title":request.data.get('title')}, status.HTTP_200_OK)

# write the business logic when a ViewSet deals with a single resource.
# class BookViewSet(viewsets.ViewSet):

# Create a class BookList that extends APIView
class BookList(APIView):
    def get(self, request):
        author = request.GET.get('author')
        if(author):
            return Response({"message":"list of books by " + author}, status.HTTP_200_OK)

        return Response({"message":"list of books"}, status.HTTP_200_OK)

    def post(self, request):
        # return Response({"message":"book created"}, status.HTTP_201_CREATED)
        title = request.data.get('title')
        return Response({"title":title}, status.HTTP_201_CREATED)

    def put(self, request):
        return Response({"message":"book updated"}, status.HTTP_200_OK)

    def delete(self, request):
        return Response({"message":"book deleted"}, status.HTTP_204_NO_CONTENT)

# Create a class to handle a single book item
class Book(APIView):
    def get(self, request, pk):
        return Response({"message":"From BOOK >> single book with id " + str(pk)}, status.HTTP_200_OK)

    def put(self, request, pk):
        return Response({"title":request.data.get('title')}, status.HTTP_200_OK)

    def delete(self, request, pk):
        return Response({"message":"book deleted"}, status.HTTP_204_NO_CONTENT)

#  Create a view function to handle Toronto Open Data API

@api_view(['GET','POST'])
def getOpenData(request):
    festival_api = "https://secure.toronto.ca/cc_sr_v1/data/edc_eventcal_APR?limit=500"
    response = requests.get(festival_api)
    return Response (response, status=status.HTTP_200_OK)