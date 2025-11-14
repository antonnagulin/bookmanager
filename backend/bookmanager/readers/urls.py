# readers/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reader_list_create, name='reader_list_create'),
    path('<int:pk>/', views.reader_detail, name='reader_detail'),
]
