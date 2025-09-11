from django import forms
from django.contrib import admin
from django.utils.html import format_html
from .models import Logo, Category, Item, ProductImage


@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="70" />', obj.image.url)
        return "-"
    image_preview.short_description = "Logo"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'lang', 'title', 'descr', 'image_preview')
    ordering = ('created_at',) 

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "-"
    image_preview.short_description = "Category Image"


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        exclude = ['heart_icon']
        widgets = {
            'color': forms.TextInput(attrs={'type': 'color'}),
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

    list_display = (
        'id', 'category_name', 'product_number', 'price',
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