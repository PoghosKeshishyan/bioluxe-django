from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import AboutUs, AboutText
from .serializers import AboutUsSerializer, AboutTextSerializer


class AbouPageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        lang = self.request.query_params.get('lang')
        if lang:
            queryset = queryset.filter(lang=lang)
        return queryset


class AboutPageTextViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutText.objects.all()
    serializer_class = AboutTextSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        lang = self.request.query_params.get('lang')
        if lang:
            queryset = queryset.filter(lang=lang)
        return queryset
