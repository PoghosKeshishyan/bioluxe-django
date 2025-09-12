from django.contrib import admin
from .models import ShopingBagPage


@admin.register(ShopingBagPage)
class ShopingBagPageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "lang",
        "title",
        "empty_error_text",
        "btn_text",
        "order_summary_field",
    )
