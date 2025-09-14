# shopping_bag_page/views.py
from rest_framework import viewsets
from .models import ShopingBagPage
from .serializers import ShopingBagPageSerializer

class ShopingBagPageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ShopingBagPage.objects.all()
    serializer_class = ShopingBagPageSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        lang = self.request.query_params.get('lang')
        if lang:
            queryset = queryset.filter(lang=lang)
        return queryset