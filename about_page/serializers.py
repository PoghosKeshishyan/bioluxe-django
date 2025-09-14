from rest_framework import serializers
from .models import AboutUs, AboutText

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'

class AboutTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutText
        fields = '__all__'
