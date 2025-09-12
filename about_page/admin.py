from django.contrib import admin
from django.utils.html import format_html
from .models import AboutUs, AboutText


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ("lang", "heading", "image_preview")

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height:50px; border-radius:4px;" />', 
                obj.image.url
            )
        return "No Image"
    image_preview.short_description = "Preview"


@admin.register(AboutText)
class AboutTextAdmin(admin.ModelAdmin):
    list_display = ("lang", "heading", "short_content1", "short_content2", "image_preview")
    list_filter = ('lang',)

    def short_content1(self, obj):
        return obj.content1[:30] + "..." if obj.content1 else ""
    short_content1.short_description = "Content1"

    def short_content2(self, obj):
        return obj.content2[:30] + "..." if obj.content2 else ""
    short_content2.short_description = "Content2"

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height:50px; border-radius:4px;" />', 
                obj.image.url
            )
        return "No Image"
    image_preview.short_description = "Preview"
