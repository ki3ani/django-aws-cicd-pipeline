from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookView.as_view(), name='book_list'),
    path('books/<int:pk>', views.BookDetail.as_view(), name='book_detail'), # new
]