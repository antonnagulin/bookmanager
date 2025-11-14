from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Reader
from .serializers import ReaderSerializer

@api_view(['GET', 'POST'])
def reader_list_create(request):
    if request.method == 'GET':
        readers = Reader.objects.all()
        serializer = ReaderSerializer(readers, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ReaderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def reader_detail(request, pk):
    try:
        reader = Reader.objects.get(pk=pk)
    except Reader.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReaderSerializer(reader)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ReaderSerializer(reader, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        reader.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
