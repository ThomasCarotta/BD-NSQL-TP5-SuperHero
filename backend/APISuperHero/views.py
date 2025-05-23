from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import SuperHero
from .serializers import SuperHeroSerializer
import traceback

class SuperHeroViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            heroes = SuperHero.objects.all()
            serializer = SuperHeroSerializer(heroes, many=True)
            return Response(serializer.data)
        except Exception as e:
            traceback.print_exc()
            return Response({"error": f"Error al obtener superhéroes: {str(e)}"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        try:
            hero = SuperHero.objects.get(id=pk)
            serializer = SuperHeroSerializer(hero)
            return Response(serializer.data)
        except SuperHero.DoesNotExist:
            return Response({"error": "Superhéroe no encontrado"},
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            traceback.print_exc()
            return Response({"error": f"Error al buscar superhéroe: {str(e)}"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        try:
            serializer = SuperHeroSerializer(data=request.data)
            if serializer.is_valid():
                hero = serializer.save()
                return Response(SuperHeroSerializer(hero).data,
                                status=status.HTTP_201_CREATED)
            print("❌ Error de validación en create():", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            traceback.print_exc()
            return Response({"error": f"Error al crear superhéroe: {str(e)}"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        try:
            hero = SuperHero.objects.get(id=pk)
            serializer = SuperHeroSerializer(hero, data=request.data)
            if serializer.is_valid():
                hero = serializer.save()
                return Response(SuperHeroSerializer(hero).data)
            print("❌ Error de validación en update():", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except SuperHero.DoesNotExist:
            return Response({"error": "Superhéroe no encontrado"},
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            traceback.print_exc()
            return Response({"error": f"Error al actualizar: {str(e)}"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
        try:
            hero = SuperHero.objects.get(id=pk)
            hero.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except SuperHero.DoesNotExist:
            return Response({"error": "Superhéroe no encontrado"},
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            traceback.print_exc()
            return Response({"error": f"Error al eliminar: {str(e)}"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
