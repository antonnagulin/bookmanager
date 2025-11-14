from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    available = serializers.ReadOnlyField()  # можно добавить вычисляемое поле

    class Meta:
        model = Book
        fields = '__all__'
