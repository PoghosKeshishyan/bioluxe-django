from rest_framework import serializers
from .models import (
    Navbar, Submenu, HeaderIcon, Language,
    SavedHeartItem, SavedBasketItem, BasketHeartViewLink
)


class SubmenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submenu
        fields = ["id", "lang", "title", "route", "created_at"]


class NavbarSerializer(serializers.ModelSerializer):
    submenus = SubmenuSerializer(many=True, read_only=True)

    class Meta:
        model = Navbar
        fields = ["id", "lang", "title", "route", "created_at", "submenus"]


class HeaderIconSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeaderIcon
        fields = "__all__"


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"


class SavedHeartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedHeartItem
        fields = "__all__"


class SavedBasketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedBasketItem
        fields = "__all__"


class BasketHeartViewLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketHeartViewLink
        fields = "__all__"
