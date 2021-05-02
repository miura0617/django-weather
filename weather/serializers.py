from rest_framework import serializers
from .models import weather

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = weather
        fields = ['id', 'location', 'weather', 'temperature']
