from rest_framework import serializers
from .models import Chicken

class ChickenSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Chicken
        fields = ("breed", "weight", "life_expectancy", "cuteness_level", "image")