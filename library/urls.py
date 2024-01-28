from django.urls import path
from . import views
from .views import debug_view, health_check

urlpatterns = [
    path('books/', views.BookView.as_view(), name='book_list'),
    path('books/<int:pk>', views.BookDetail.as_view(), name='book_detail'), # new
    path('debug/', debug_view, name='debug_view'),
    path('/health-check', health_check, name='health_check'),
]