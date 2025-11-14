from django.urls import path
from . import views

urlpatterns = [
    path('', views.loan_list_create, name='loan_list_create'),
    path('<int:pk>/return/', views.loan_return, name='loan_return'),
]
