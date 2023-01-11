from rest_framework import serializers
from .models import Breed,Dog

class BreedSerializers(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = "__all__"

class DogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = "__all__"

