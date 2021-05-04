from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import GroupSerializer, CharacteristicSerializer, AnimalSerializer
from .models import Animal, Group, Characteristic


class AnimalView(APIView):
    def get(self, request):
        queryset = Animal.objects.all()
        serializer = AnimalSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AnimalSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.data
        group = data.pop('group')
        characteristic_list = data.pop('characteristic_set')

        group_db = Group.objects.get_or_create(**group)[0]
        animal = Animal.objects.create(**data, group=group_db)

        for each_characteristic in characteristic_list:
            characteristic_db = Characteristic.objects.get_or_create(**each_characteristic)[0]
            animal.characteristic_set.add(characteristic_db)       

        serializer = AnimalSerializer(animal)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, animal_id):
        Animal.objects.get(id=animal_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)