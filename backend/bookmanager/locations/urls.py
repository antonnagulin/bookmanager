from django.urls import path
from . import views

app_name = "locations"

urlpatterns = [
    # LocationRoot (универсальный корень: библиотека, склад, магазин и т.д.)
    path('roots/', views.root_list_create, name='root_list_create'),
    path('roots/<int:pk>/', views.root_detail, name='root_detail'),

    # Racks
    path('racks/', views.rack_list_create, name='rack_list'),
    path('racks/<int:pk>/', views.rack_detail, name='rack_detail'),
    path('roots/<int:root_id>/racks/', views.rack_list_create, name='root_racks'),

    # Sections
    path('sections/', views.sections_list_create, name='section_list'),
    path('sections/<int:pk>/', views.sections_detail, name='section_detail'),
    path('racks/<int:rack_id>/sections/', views.sections_list_create, name='rack_sections'),
]


