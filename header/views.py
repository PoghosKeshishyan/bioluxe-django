from rest_framework import viewsets
from .models import (
    Navbar, Submenu, HeaderIcon, Language,
    SavedHeartItem, SavedBasketItem, BasketHeartViewLink
)
from .serializers import (
    NavbarSerializer, SubmenuSerializer, HeaderIconSerializer,
    LanguageSerializer, SavedHeartItemSerializer,
    SavedBasketItemSerializer, BasketHeartViewLinkSerializer
)


class NavbarViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NavbarSerializer

    def get_queryset(self):
        qs = Navbar.objects.all().order_by("created_at")
        lang = self.request.query_params.get("lang")
        if lang:
            qs = qs.filter(lang=lang)
        return qs


class SubmenuViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SubmenuSerializer

    def get_queryset(self):
        qs = Submenu.objects.all().order_by("created_at")
        lang = self.request.query_params.get("lang")
        if lang:
            qs = qs.filter(lang=lang)
        return qs


class HeaderIconViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = HeaderIconSerializer

    def get_queryset(self):
        return HeaderIcon.objects.all().order_by("created_at")


class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LanguageSerializer

    def get_queryset(self):
        qs = Language.objects.all().order_by("created_at")
        lang = self.request.query_params.get("lang")
        if lang:
            qs = qs.filter(lang=lang)
        return qs


class SavedHeartItemViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SavedHeartItemSerializer

    def get_queryset(self):
        qs = SavedHeartItem.objects.all().order_by("created_at")
        lang = self.request.query_params.get("lang")
        if lang:
            qs = qs.filter(lang=lang)
        return qs


class SavedBasketItemViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SavedBasketItemSerializer

    def get_queryset(self):
        qs = SavedBasketItem.objects.all().order_by("created_at")
        lang = self.request.query_params.get("lang")
        if lang:
            qs = qs.filter(lang=lang)
        return qs


class BasketHeartViewLinkViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BasketHeartViewLinkSerializer

    def get_queryset(self):
        qs = BasketHeartViewLink.objects.all().order_by("created_at")
        lang = self.request.query_params.get("lang")
        if lang:
            qs = qs.filter(lang=lang)
        return qs
