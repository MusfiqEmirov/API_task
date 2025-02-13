from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from library.models import Book
from library.serializers import BookSerializer


class BookAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()  # Butun kitablari aliriq
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
class BookIdDetailView(APIView):
    def get(self, request, id):
        try:
            book = Book.objects.get(id=id) 
        except Book.DoesNotExist:
            raise NotFound("Book not found") 

        serializer = BookSerializer(book)
        return Response(serializer.data)    
    

class BookSlugDeatil(APIView):
    def get(self, request, slug):
        try:
            book = Book.objects.get(slug=slug)  
        except Book.DoesNotExist:
            raise NotFound("Book not found")  

        serializer = BookSerializer(book)
        return Response(serializer.data)