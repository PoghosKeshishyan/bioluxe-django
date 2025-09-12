from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Navbar, Submenu, HeaderIcon, Language,
    SavedHeartItem, SavedBasketItem, BasketHeartViewLink
)

admin.site.register(BasketHeartViewLink)

class SubmenuInline(admin.TabularInline):
    model = Submenu
    extra = 1
    fields = ('lang', 'title', 'route')


@admin.register(Navbar)
class NavbarAdmin(admin.ModelAdmin):
    ordering = ('created_at',) 
    inlines = [SubmenuInline]
    
    
@admin.register(HeaderIcon)
class HeaderIconAdmin(admin.ModelAdmin):
    list_display = ('id', 'search_icon_display', 'heart_icon_display', 'cart_icon_display')
    
    def _preview(self, obj, field_name):
        file = getattr(obj, field_name)
        if file:
            return format_html('<img src="{}" width="70" />', file.url)
        return "-"
    
    def search_icon_display(self, obj):
        return self._preview(obj, 'search_icon')
    search_icon_display.short_description = 'Search Icon'

    def heart_icon_display(self, obj):
        return self._preview(obj, 'heart_icon')
    heart_icon_display.short_description = 'Heart Icon'

    def cart_icon_display(self, obj):
        return self._preview(obj, 'cart_icon')
    cart_icon_display.short_description = 'Cart Icon'
    

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'lang', 'label', 'image_display')
    ordering = ('created_at',) 
    
    def image_display(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="70" />', obj.image.url)
        return "-"
    image_display.short_description = 'Image'
    

@admin.register(SavedHeartItem)
class SavedHeartItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "lang",
        "heading",
        "add_button_icon",
        "add_button_text",
        "remove_button_icon",
        "remove_button_text",
    )
    ordering = ("created_at",)


@admin.register(SavedBasketItem)
class SavedBasketItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "lang",
        "heading",
        "quantity",
        "remove_button_icon",
        "remove_button_text",
    )
    ordering = ("created_at",)