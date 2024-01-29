from .models import Book, Author, Review
from rest_framework import generics
from .serializers import BookSerializer, AuthorSerializer, ReviewSerializer
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
class AuthorView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ReviewView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

def debug_view(request):
    # Print HTTP_HOST and request headers for debugging
    print("HTTP_HOST:", request.get_host())
    print("Request Headers:", request.headers)

def home(request):
    return render(request, 'home.html')
