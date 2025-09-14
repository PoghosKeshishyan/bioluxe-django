from rest_framework import viewsets
from .models import FooterInfo, FooterSocialLink, FooterPrivacyPolicy
from .serializers import FooterInfoSerializer, FooterSocialLinkSerializer, FooterPrivacyPolicySerializer

class FooterInfoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FooterInfoSerializer

    def get_queryset(self):
        qs = FooterInfo.objects.all().order_by("created_at")
        lang = self.request.query_params.get("lang")
        if lang:
            qs = qs.filter(lang=lang)
        return qs

class FooterSocialLinkViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FooterSocialLinkSerializer

    def get_queryset(self):
        return FooterSocialLink.objects.all().order_by("created_at")

class FooterPrivacyPolicyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FooterPrivacyPolicySerializer

    def get_queryset(self):
        qs = FooterPrivacyPolicy.objects.all().order_by("created_at")
        lang = self.request.query_params.get("lang")
        if lang:
            qs = qs.filter(lang=lang)
        return qs
