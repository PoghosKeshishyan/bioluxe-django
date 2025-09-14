# home_page/views.py
from rest_framework import viewsets
from .models import (
    Slider, SliderIcon, AboutUs, PopularItemHeading, 
    NewArrivalsHeading, ContactUs, 
    CategoriesHeading, PartnersHeading, Partner
)
from .serializers import (
    SliderSerializer, SliderIconSerializer, AboutUsSerializer,
    PopularItemHeadingSerializer,
    NewArrivalsHeadingSerializer, ContactUsSerializer, 
    CategoriesHeadingSerializer, PartnersHeadingSerializer, 
    PartnerSerializer
)
from global_data.models import Item
from global_data.serializers import ItemSerializer


class SliderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        lang = self.request.query_params.get('lang')
        if lang:
            queryset = queryset.filter(lang=lang)
        return queryset

class SliderIconViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SliderIcon.objects.all()
    serializer_class = SliderIconSerializer

class AboutUsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        lang = self.request.query_params.get('lang')
        if lang:
            queryset = queryset.filter(lang=lang)
        return queryset

class PopularItemHeadingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PopularItemHeading.objects.all()
    serializer_class = PopularItemHeadingSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        lang = self.request.query_params.get('lang')
        if lang:
            queryset = queryset.filter(lang=lang)
        return queryset

class PopularItemViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ItemSerializer
    
    def get_queryset(self):
        queryset = Item.objects.filter(is_popular=True)
        return queryset.prefetch_related('images')

class NewArrivalsHeadingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NewArrivalsHeading.objects.all()
    serializer_class = NewArrivalsHeadingSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        lang = self.request.query_params.get('lang')
        if lang:
            queryset = queryset.filter(lang=lang)
        return queryset

class ContactUsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        lang = self.request.query_params.get('lang')
        if lang:
            queryset = queryset.filter(lang=lang)
        return queryset

class CategoriesHeadingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CategoriesHeading.objects.all()
    serializer_class = CategoriesHeadingSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        lang = self.request.query_params.get('lang')
        if lang:
            queryset = queryset.filter(lang=lang)
        return queryset

class PartnersHeadingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PartnersHeading.objects.all()
    serializer_class = PartnersHeadingSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        lang = self.request.query_params.get('lang')
        if lang:
            queryset = queryset.filter(lang=lang)
        return queryset

class PartnerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer