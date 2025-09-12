from django.contrib import admin
from django.utils.html import format_html

from .models import (
    Slider, SliderIcon, AboutUs, PopularItemHeading, NewArrivalsHeading,
    ContactUs, CategoriesHeading, PartnersHeading, Partner
)


admin.site.register(PopularItemHeading)
admin.site.register(NewArrivalsHeading)
admin.site.register(CategoriesHeading)
admin.site.register(PartnersHeading)


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ("lang", "heading", "btn_text", "btn_url", "image1_preview", "image2_preview")

    def image1_preview(self, obj):
        if obj.image_1:
            return format_html('<img src="{}" style="height:60px; border-radius:5px;" />', obj.image_1.url)
        return "No Image"
    image1_preview.short_description = "Image 1"

    def image2_preview(self, obj):
        if obj.image_2:
            return format_html('<img src="{}" style="height:60px; border-radius:5px;" />', obj.image_2.url)
        return "No Image"
    image2_preview.short_description = "Image 2"
    
    
@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ("lang", "heading", "map_url", "map_image_preview")

    def map_image_preview(self, obj):
        if obj.map_image:
            return format_html('<img src="{}" style="height:80px; border-radius:5px;" />', obj.map_image.url)
        return "No Image"
    map_image_preview.short_description = "Map Image"
    

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ("id", "image_preview")

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:80px; border-radius:5px;" />', obj.image.url)
        return "No Image"
    image_preview.short_description = "Partner Image"
    

@admin.register(SliderIcon)
class SliderIconAdmin(admin.ModelAdmin):
    list_display = ("id", "cloud_icon_preview", "left_arrow_icon_preview", "right_arrow_icon_preview")

    def cloud_icon_preview(self, obj):
        if obj.cloud_icon:
            return format_html('<img src="{}" style="height:50px; border-radius:5px;" />', obj.cloud_icon.url)
        return "No Image"
    cloud_icon_preview.short_description = "Cloud Icon"

    def left_arrow_icon_preview(self, obj):
        if obj.left_arrow_icon:
            return format_html('<img src="{}" style="height:50px; border-radius:5px;" />', obj.left_arrow_icon.url)
        return "No Image"
    left_arrow_icon_preview.short_description = "Left Arrow Icon"

    def right_arrow_icon_preview(self, obj):
        if obj.right_arrow_icon:
            return format_html('<img src="{}" style="height:50px; border-radius:5px;" />', obj.right_arrow_icon.url)
        return "No Image"
    right_arrow_icon_preview.short_description = "Right Arrow Icon"


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ("lang", "title", "btn_text", "btn_url", "background_image_preview", "image_preview")
    list_filter = ('lang',)
    ordering = ('created_at',)

    def background_image_preview(self, obj):
        if obj.background_image:
            return format_html('<img src="{}" style="height:80px; border-radius:5px;" />', obj.background_image.url)
        return "No Image"
    background_image_preview.short_description = "Background Image"

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:80px; border-radius:5px;" />', obj.image.url)
        return "No Image"
    image_preview.short_description = "Slider Image"