from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import SuperHero
from .serializers import SuperHeroSerializer

class SuperHeroViewSet(viewsets.ViewSet):

    def list(self, request):
        heroes = SuperHero.objects.all()
        serializer = SuperHeroSerializer(heroes, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            hero = SuperHero.objects.get(id=pk)
        except SuperHero.DoesNotExist:
            return Response({"error": "Hero not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = SuperHeroSerializer(hero)
        return Response(serializer.data)

    def create(self, request):
        serializer = SuperHeroSerializer(data=request.data)
        if serializer.is_valid():
            hero = serializer.save()
            return Response(SuperHeroSerializer(hero).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            hero = SuperHero.objects.get(id=pk)
        except SuperHero.DoesNotExist:
            return Response({"error": "Hero not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = SuperHeroSerializer(hero, data=request.data)
        if serializer.is_valid():
            hero = serializer.save()
            return Response(SuperHeroSerializer(hero).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            hero = SuperHero.objects.get(id=pk)
            hero.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except SuperHero.DoesNotExist:
            return Response({"error": "Hero not found"}, status=status.HTTP_404_NOT_FOUND)
