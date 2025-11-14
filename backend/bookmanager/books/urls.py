from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list_create, name='book_list_create'),
    path('<int:pk>/', views.book_detail, name='book_detail'),
]
