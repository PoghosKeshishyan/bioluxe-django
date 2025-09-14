# home_page/serializers.py
from rest_framework import serializers
from .models import (
    Slider, SliderIcon, AboutUs, PopularItemHeading, 
    NewArrivalsHeading, ContactUs,
    CategoriesHeading, PartnersHeading, Partner
)

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'

class SliderIconSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderIcon
        fields = '__all__'

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'

class PopularItemHeadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularItemHeading
        fields = '__all__'

class NewArrivalsHeadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewArrivalsHeading
        fields = '__all__'

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'

class CategoriesHeadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriesHeading
        fields = '__all__'

class PartnersHeadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnersHeading
        fields = '__all__'

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'