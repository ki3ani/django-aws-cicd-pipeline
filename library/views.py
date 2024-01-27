from .models import Book
from rest_framework import generics
from .serializers import BookSerializer
from django.http import HttpResponse


# Create your views here.
class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class BookDetail(generics.RetrieveUpdateDestroyAPIView): # new
    queryset = Book.objects.all()
    serializer_class = BookSerializer


def debug_view(request):
    # Print HTTP_HOST and request headers for debugging
    print("HTTP_HOST:", request.get_host())
    print("Request Headers:", request.headers)

    # Rest of your view code (or just return a simple response for testing)
    return HttpResponse("Debug view response")
