from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import LocationRoot, Rack, Section
from .serializers import LocationRootSerializer, RackSerializer, SectionSerializer


# ----------------- LocationRoot -----------------
@api_view(['GET', 'POST'])
def root_list_create(request):
    if request.method == 'GET':
        root = LocationRoot.objects.all()
        serializer = LocationRootSerializer(root, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = LocationRootSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def root_detail(request, pk):
    try:
        root = LocationRoot.objects.get(pk=pk)
    except LocationRoot.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LocationRootSerializer(root)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = LocationRootSerializer(root, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        root.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ----------------- Rack -----------------
@api_view(['GET', 'POST'])
def rack_list_create(request, root_id=None):
    if root_id:
        rack = Rack.objects.filter(root_id=root_id)
    else:
        rack = Rack.objects.all()

    if request.method == 'GET':
        serializer = RackSerializer(rack, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        data = request.data.copy()
        if root_id:
            data['root'] = root_id
        serializer = RackSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def rack_detail(request, pk):
    try:
        rack = Rack.objects.get(pk=pk)
    except Rack.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RackSerializer(rack)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = RackSerializer(rack, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        rack.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ----------------- SECTIONS ----------------
@api_view(['GET', 'POST'])
def sections_list_create(request, rack_id=None):
    if rack_id:
        sections = Section.objects.filter(rack_id=rack_id)
    else:
        sections = Section.objects.all()

    if request.method == 'GET':
        serializer = SectionSerializer(sections, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data.copy()
        if rack_id:
            data['rack'] = rack_id
        serializer = SectionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def sections_detail(request, pk):
    try:
        sections = Section.objects.get(pk=pk)
    except Section.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SectionSerializer(sections)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = SectionSerializer(sections, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        sections.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
