from rest_framework import viewsets
from .models import ContactTitle, ContactInfo, ContactForm
from .serializers import ContactTitleSerializer, ContactInfoSerializer, ContactFormSerializer

class ContactTitleViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ContactTitleSerializer

    def get_queryset(self):
        qs = ContactTitle.objects.all().order_by("id")
        lang = self.request.query_params.get("lang")
        if lang:
            qs = qs.filter(lang=lang)
        return qs

class ContactInfoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ContactInfoSerializer

    def get_queryset(self):
        qs = ContactInfo.objects.all().order_by("id")
        lang = self.request.query_params.get("lang")
        if lang:
            qs = qs.filter(lang=lang)
        return qs

class ContactFormViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ContactFormSerializer

    def get_queryset(self):
        qs = ContactForm.objects.all().order_by("id")
        lang = self.request.query_params.get("lang")
        if lang:
            qs = qs.filter(lang=lang)
        return qs
