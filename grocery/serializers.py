from rest_framework import serializers
from .models import Food

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = [
            'year', 'model', 'description', 'recieved', 'updated'
        ]
