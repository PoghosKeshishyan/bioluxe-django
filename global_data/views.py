# global_data/views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import (
    Logo, Category, Categories_link, Item, ProductImage, ItemHeader,
    ItemPageField, ItemLink, ItemFaqHeading, ItemFaq,
    LikedProductHeading, InfoAboutDelivery
)
from .serializers import (
    LogoSerializer, CategorySerializer, CategoriesLinkSerializer,
    ItemSerializer, ProductImageSerializer, ItemHeaderSerializer,
    ItemPageFieldSerializer, ItemLinkSerializer, ItemFaqHeadingSerializer,
    ItemFaqSerializer, LikedProductHeadingSerializer, InfoAboutDeliverySerializer
)

class LogoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        lang = self.request.query_params.get('lang')
        if lang:
            queryset = queryset.filter(lang=lang)
        return queryset

class CategoriesLinkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Categories_link.objects.all()
    serializer_class = CategoriesLinkSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        lang = self.request.query_params.get('lang')
        if lang:
            queryset = queryset.filter(lang=lang)
        return queryset

class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        
        category_name = self.request.query_params.get('category')
        if category_name:
            queryset = queryset.filter(category_name=category_name)
        
        return queryset

    def retrieve(self, request, *args, **kwargs):
        item = get_object_or_404(Item, pk=kwargs["pk"])
        item_serializer = self.get_serializer(item)

        related_items = Item.objects.filter(group_code=item.group_code).exclude(id=item.id)
        related_serializer = self.get_serializer(related_items, many=True)

        return Response({
            "item": item_serializer.data,
            "relatedItems": related_serializer.data
        })

    @action(detail=False, methods=['get'], url_path='latest')
    def get_latest_items(self, request):
        latest_items = Item.objects.all().order_by('-created_at')[:4]
        serializer = self.get_serializer(latest_items, many=True)
        return Response(serializer.data)
    
class ProductImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

class ItemHeaderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ItemHeader.objects.all()
    serializer_class = ItemHeaderSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        lang = self.request.query_params.get('lang')
        category_name = self.request.query_params.get('category_name')
        
        if lang:
            queryset = queryset.filter(lang=lang)
        if category_name:
            queryset = queryset.filter(category_name=category_name)
            
        return queryset

class ItemPageFieldViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ItemPageField.objects.all()
    serializer_class = ItemPageFieldSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        lang = self.request.query_params.get('lang')
        if lang:
            queryset = queryset.filter(lang=lang)
        return queryset

class ItemLinkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ItemLink.objects.all()
    serializer_class = ItemLinkSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        lang = self.request.query_params.get('lang')
        if lang:
            queryset = queryset.filter(lang=lang)
        return queryset

class ItemFaqHeadingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ItemFaqHeading.objects.all()
    serializer_class = ItemFaqHeadingSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        lang = self.request.query_params.get('lang')
        if lang:
            queryset = queryset.filter(lang=lang)
        return queryset

class ItemFaqViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ItemFaq.objects.all()
    serializer_class = ItemFaqSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        lang = self.request.query_params.get('lang')
        if lang:
            queryset = queryset.filter(lang=lang)
        return queryset

class LikedProductHeadingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LikedProductHeading.objects.all()
    serializer_class = LikedProductHeadingSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        lang = self.request.query_params.get('lang')
        if lang:
            queryset = queryset.filter(lang=lang)
        return queryset

class InfoAboutDeliveryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InfoAboutDelivery.objects.all()
    serializer_class = InfoAboutDeliverySerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        lang = self.request.query_params.get('lang')
        if lang:
            queryset = queryset.filter(lang=lang)
        return queryset