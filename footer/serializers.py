from rest_framework import serializers
from .models import FooterInfo, FooterSocialLink, FooterPrivacyPolicy

class FooterInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterInfo
        fields = "__all__"

class FooterSocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterSocialLink
        fields = "__all__"

class FooterPrivacyPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterPrivacyPolicy
        fields = "__all__"
