from django import forms
from django.contrib import admin
from django.utils.html import format_html
import json
from .models import (
    Logo, Category, Categories_link, Item, ProductImage, 
    ItemHeader, ItemPageField, ItemLink, ItemFaqHeading, ItemFaq, 
    LikedProductHeading, InfoAboutDelivery
)

# Register simple models
admin.site.register(Categories_link)
admin.site.register(ItemPageField)
admin.site.register(ItemLink)
admin.site.register(ItemFaqHeading)
admin.site.register(ItemFaq)
admin.site.register(LikedProductHeading)

# -------------------------
# Logo admin
# -------------------------
@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="70" />', obj.image.url)
        return "-"
    image_preview.short_description = "Logo"

# -------------------------
# Category admin
# -------------------------
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'lang', 'title', 'descr', 'image_preview')
    list_filter = ('category_name',)
    ordering = ('created_at',) 

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "-"
    image_preview.short_description = "Image"

# -------------------------
# Item admin
# -------------------------
class JSONKeyValueWidget(forms.Widget):
    template_name = "admin/json_key_value_widget.html"

    def format_value(self, value):
        """Վերածում JSON dict-ը Python list of dicts"""
        if value is None:
            return []
        if isinstance(value, str):
            try:
                value = json.loads(value)
            except Exception:
                return []
        # Եթե dict է, դարձնում ենք list of dicts
        if isinstance(value, dict):
            return [{"key": k, "value": v} for k, v in value.items()]
        return value

    def value_from_datadict(self, data, files, name):
        """Վերցնում ենք բոլոր key-value զույգերը"""
        keys = data.getlist(f"{name}_key")
        values = data.getlist(f"{name}_value")
        result = {}
        for k, v in zip(keys, values):
            if k.strip():  # key դատարկ չէ
                result[k] = v
        return result

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        exclude = ['heart_icon']
        widgets = {
            'color': forms.TextInput(attrs={'type': 'color'}),
            'title': JSONKeyValueWidget(),
            'btn_text': JSONKeyValueWidget(),
            'descr': JSONKeyValueWidget(),
            'product_material': JSONKeyValueWidget(),
            'about_delivery': JSONKeyValueWidget(),
        }

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="70" />', obj.image.url)
        return "-"
    image_preview.short_description = "Preview"


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    form = ItemForm
    list_filter = ('category_name', 'is_popular')
    list_display = (
        'id', 'is_popular', 'category_name', 'product_number', 'price',
        'color_display', 'size', 'group_code', 'first_image_preview',
    )
    ordering = ('created_at',)
    inlines = [ProductImageInline]
    
    
    def color_display(self, obj):
        return format_html(
            '<div style="display:flex; align-items:center;">'
            '<div style="width: 50px; height: 20px; background-color: {}; border: 1px solid #000; margin-right: 5px;"></div>'
            '<span>{}</span>'
            '</div>',
            obj.color,
            obj.color 
        )
    color_display.short_description = 'Color'

    def first_image_preview(self, obj):
        first_image = ProductImage.objects.filter(product=obj).first()
        if first_image and first_image.image:
            return format_html(
                '<div style="display:flex; align-items:center;">'
                '<img src="{}" width="60" style="margin-right:5px;"/>'
                '</div>',
                first_image.image.url,
            )
        return "-"
    first_image_preview.short_description = "Image"

# -------------------------
# ItemHeader admin
# -------------------------
@admin.register(ItemHeader)
class ItemHeaderAdmin(admin.ModelAdmin):
    list_display = ('id', 'lang', 'category_name', 'title', 'descr', 'image_preview')
    search_fields = ('title', 'descr', 'category_name', 'lang')
    list_filter = ('lang', 'category_name')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="70" style="object-fit:cover;"/>', obj.image.url)
        return "-"
    image_preview.short_description = "Image"

# -------------------------
# InfoAboutDelivery admin
# -------------------------
class JSONListWidget(forms.Widget):
    """Custom JSON widget for InfoAboutDelivery"""
    template_name = "admin/json_list_widget.html"

    def format_value(self, value):
        if value is None:
            return []
        if isinstance(value, str):
            try:
                return json.loads(value)
            except Exception:
                return []
        return value

    def value_from_datadict(self, data, files, name):
        values = data.getlist(name)
        return [v for v in values if v.strip()]

class InfoAboutDeliveryForm(forms.ModelForm):
    texts = forms.Field(widget=JSONListWidget(), required=False)

    class Meta:
        model = InfoAboutDelivery
        fields = "__all__"

@admin.register(InfoAboutDelivery)
class InfoAboutDeliveryAdmin(admin.ModelAdmin):
    form = InfoAboutDeliveryForm
