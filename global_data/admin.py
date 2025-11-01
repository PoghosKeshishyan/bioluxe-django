from django import forms
from django.contrib import admin
from django.utils.html import format_html
import json
from .models import (
    Logo, Category, Categories_link, Item, ItemAboutDelivery, ProductImage, 
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
        if value is None:
            return []
        if isinstance(value, str):
            try:
                value = json.loads(value)
            except Exception:
                return []
        if isinstance(value, dict):
            return [{"key": k, "value": v} for k, v in value.items()]
        return value

    def value_from_datadict(self, data, files, name):
        keys = data.getlist(f"{name}_key")
        values = data.getlist(f"{name}_value")
        result = {}
        for k, v in zip(keys, values):
            if k.strip():
                result[k] = v
        return result

class JSONKeyValueWidgetTextarea(forms.Widget):
    template_name = "admin/json_key_value_widget_textarea.html"

    def format_value(self, value):
        if value is None:
            return []
        if isinstance(value, str):
            try:
                value = json.loads(value)
            except Exception:
                return []
        if isinstance(value, dict):
            return [{"key": k, "value": v} for k, v in value.items()]
        return value

    def value_from_datadict(self, data, files, name):
        keys = data.getlist(f"{name}_key")
        values = data.getlist(f"{name}_value")
        result = {}
        for k, v in zip(keys, values):
            if k.strip():
                result[k] = v
        return result



class ItemForm(forms.ModelForm):
    category_name = forms.ModelChoiceField(
        queryset=Category.objects.filter(lang='en'),
        required=False,
        label='Category',
        widget=forms.Select(attrs={'class': 'vSelect'})
    )

    class Meta:
        model = Item
        fields = '__all__'
        exclude = ['heart_icon']
        widgets = {
            'title': JSONKeyValueWidget(),
            'btn_text': JSONKeyValueWidget(),
            'descr': JSONKeyValueWidget(),
            'product_material': JSONKeyValueWidget(),
            'about_delivery': JSONKeyValueWidget(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk and self.instance.category_name:
            try:
                category = Category.objects.get(title=self.instance.category_name, lang='en')
                self.initial['category_name'] = category.id
            except Category.DoesNotExist:
                pass

    def save(self, commit=True):
        instance = super().save(commit=False)
        category = self.cleaned_data.get('category_name')
        if category:
            instance.category_name = category.title
        if commit:
            instance.save()
        return instance 
    

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    max_num = 10
    readonly_fields = ('image_preview',)
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'is_general':
            # Create custom radio buttons with only one choice (True)
            kwargs['widget'] = forms.RadioSelect(
                choices=[(True, '⭐ Հիմնական նկար')],
                attrs={'class': 'general-image-radio'}
            )
        return super().formfield_for_dbfield(db_field, **kwargs)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="70" />', obj.image.url)
        return "-"
    image_preview.short_description = "Preview"




@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    form = ItemForm
    list_filter = ('category_name', 'is_popular', 'is_new_arrival')
    list_display = (
        'id', 'is_popular', 'is_new_arrival','category_name', 'product_number', 'price',
        'color_display', 'size', 'group_code', 'first_image_preview',
    )
    ordering = ('-created_at',)
    inlines = [ProductImageInline]
    
    class Media:
        js = ('admin/js/product_image_radio.js',)
        css = {
            'all': ('admin/css/product_image.css',)
        }
    
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
        general_image = obj.images.filter(is_general=True).first()
        if general_image and general_image.image:
            return format_html(
                '<img src="{}" width="60" style="border: 2px solid #4CAF50;"/>',
                general_image.image.url,
            )
        
        # Fallback to first image
        first_image = obj.images.first()
        if first_image and first_image.image:
            return format_html(
                '<img src="{}" width="60" style="border: 1px solid #ddd;"/>',
                first_image.image.url,
            )
        return "-"
    first_image_preview.short_description = "Image"



class ItemAboutDeliveryForm(forms.ModelForm):
    class Meta:
        model = ItemAboutDelivery
        fields = '__all__'
        widgets = {
            'about_delivery': JSONKeyValueWidgetTextarea(),
        }


@admin.register(ItemAboutDelivery)
class ItemAboutDeliveryAdmin(admin.ModelAdmin):
    form = ItemAboutDeliveryForm



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
