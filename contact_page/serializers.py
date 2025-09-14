from rest_framework import serializers
from .models import ContactTitle, ContactInfo, ContactForm

class ContactTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactTitle
        fields = "__all__"

class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = "__all__"

class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = "__all__"
