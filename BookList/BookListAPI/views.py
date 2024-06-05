from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

# Rest framework DRF imports
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


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
    # def put(self, request, pk):
    #      return Response({"title":request.data.get('title')}, status.HTTP_200_OK)


