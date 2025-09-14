# shopping_bag_page/serializers.py
from rest_framework import serializers
from .models import ShopingBagPage

class ShopingBagPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopingBagPage
        fields = '__all__'