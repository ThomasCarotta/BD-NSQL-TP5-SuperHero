from rest_framework import serializers
from .models import SuperHero

class SuperHeroSerializer(serializers.Serializer):
    id = serializers.SerializerMethodField(read_only=True)
    name = serializers.CharField()
    real_name = serializers.CharField(allow_blank=True, required=False)
    debut_year = serializers.IntegerField()
    house = serializers.ChoiceField(choices=["Marvel", "DC"])
    biography = serializers.CharField()
    equipment = serializers.CharField(allow_blank=True, required=False)
    images = serializers.ListField(child=serializers.CharField())

    def get_id(self, obj):
        # Maneja tanto objetos SuperHero como diccionarios
        if hasattr(obj, 'id'):
            return str(obj.id)
        return str(obj.get('_id', ''))

    def create(self, validated_data):
        return SuperHero(**validated_data).save()

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance