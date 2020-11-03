from rest_framework import serializers
from .models.greeting import Greeting


class GreetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Greeting
        fields = ('name', 'time')
