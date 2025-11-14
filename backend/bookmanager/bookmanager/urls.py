from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', include('books.urls')),
    path('reader/', include('readers.urls')),
    path('loan/', include('loans.urls')),
]
