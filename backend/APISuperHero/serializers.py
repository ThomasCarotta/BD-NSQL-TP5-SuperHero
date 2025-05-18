from rest_framework import serializers
from .models import SuperHero

class SuperHeroSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    real_name = serializers.CharField(allow_blank=True, required=False)
    debut_year = serializers.IntegerField()
    house = serializers.ChoiceField(choices=["Marvel", "DC"])
    biography = serializers.CharField()
    equipment = serializers.CharField(allow_blank=True, required=False)
    images = serializers.ListField(child=serializers.CharField())

    def create(self, validated_data):
        return SuperHero(**validated_data).save()

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
