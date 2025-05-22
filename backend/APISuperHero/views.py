from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import SuperHero
from .serializers import SuperHeroSerializer

class SuperHeroViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            heroes = SuperHero.objects.all()
            serializer = SuperHeroSerializer(heroes, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        try:
            hero = SuperHero.objects.get(id=pk)
            serializer = SuperHeroSerializer(hero)
            return Response(serializer.data)
        except SuperHero.DoesNotExist:
            return Response({"error": "Hero not found"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = SuperHeroSerializer(data=request.data)
        if serializer.is_valid():
            hero = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            hero = SuperHero.objects.get(id=pk)
            serializer = SuperHeroSerializer(hero, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except SuperHero.DoesNotExist:
            return Response({"error": "Hero not found"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            hero = SuperHero.objects.get(id=pk)
            hero.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except SuperHero.DoesNotExist:
            return Response({"error": "Hero not found"}, status=status.HTTP_404_NOT_FOUND)