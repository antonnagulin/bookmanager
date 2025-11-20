from rest_framework import serializers
from .models import LocationRoot, Rack, Section


class LocationRootSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationRoot
        fields = ['id', 'name', 'description']


class RackSerializer(serializers.ModelSerializer):
    root_name = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
        source='root'
    )

    class Meta:
        model = Rack
        fields = ['id', 'number', 'root', 'root_name']


class SectionSerializer(serializers.ModelSerializer):
    rack_number = serializers.SlugRelatedField(
        read_only=True,
        slug_field='number',
        source='rack'
    )

    class Meta:
        model = Section
        fields = ['id', 'number', 'rack', 'rack_number']
