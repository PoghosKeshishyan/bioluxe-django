# global_data/serializers.py
from rest_framework import serializers
from .models import (
    Logo, Category, Categories_link, Item, ProductImage, ItemHeader,
    ItemPageField, ItemLink, ItemFaqHeading, ItemFaq,
    LikedProductHeading, InfoAboutDelivery
)

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'product']

class ItemSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Item
        fields = '__all__'

class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CategoriesLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories_link
        fields = '__all__'

class ItemHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemHeader
        fields = '__all__'

class ItemPageFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPageField
        fields = '__all__'

class ItemLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemLink
        fields = '__all__'

class ItemFaqHeadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemFaqHeading
        fields = '__all__'

class ItemFaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemFaq
        fields = '__all__'

class LikedProductHeadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikedProductHeading
        fields = '__all__'

class InfoAboutDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoAboutDelivery
        fields = '__all__'