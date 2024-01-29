from django.urls import path
from . import views
from .views import debug_view, home

urlpatterns = [
    path('authors/', views.AuthorView.as_view(), name='author_list'),
    path('authors/<int:pk>', views.AuthorDetail.as_view(), name='author_detail'),
    path('books/', views.BookView.as_view(), name='book_list'),
    path('books/<int:pk>', views.BookDetail.as_view(), name='book_detail'),
    path('reviews/', views.ReviewView.as_view(), name='review_list'),
    path('reviews/<int:pk>', views.ReviewDetail.as_view(), name='review_detail'),
    path('debug/', debug_view, name='debug_view'),
    path('', home, name='home'),
]