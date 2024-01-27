from .models import Book
from rest_framework import generics
from .serializers import BookSerializer



# Create your views here.
class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class BookDetail(generics.RetrieveUpdateDestroyAPIView): # new
    queryset = Book.objects.all()
    serializer_class = BookSerializer