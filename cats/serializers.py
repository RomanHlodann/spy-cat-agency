import requests

from rest_framework import serializers

from cats.models import Cat


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ('id', 'name', 'years_of_experience', 'breed', 'salary')

    def validate_breed(self, value):
        response = requests.get(f"https://api.thecatapi.com/v1/breeds/search", params={"q": value})

        if not response.json():
            raise serializers.ValidationError("Breed name not found")

        return value


class CatUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ('id', 'salary',)
