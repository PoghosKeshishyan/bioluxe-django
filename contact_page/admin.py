from django.contrib import admin
from django.utils.html import format_html
from .models import ContactTitle, ContactInfo, ContactForm


admin.site.register(ContactForm)


@admin.register(ContactTitle)
class ContactTitleAdmin(admin.ModelAdmin):
    list_display = ("lang", "title", "image_preview")

    def image_preview(self, obj):
        if obj.image_url:
            return format_html('<img src="{}" style="width: 100px; height:auto;" />', obj.image_url.url)
        return "No Image"
    image_preview.short_description = "Image"


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ("lang", "address", "phone", "email", "address_icon_preview", "phone_icon_preview", "email_icon_preview")

    def address_icon_preview(self, obj):
        if obj.address_icon:
            return format_html('<img src="{}" style="width: 40px; height:auto;" />', obj.address_icon.url)
        return "No Icon"
    address_icon_preview.short_description = "Address Icon"

    def phone_icon_preview(self, obj):
        if obj.phone_icon:
            return format_html('<img src="{}" style="width: 40px; height:auto;" />', obj.phone_icon.url)
        return "No Icon"
    phone_icon_preview.short_description = "Phone Icon"

    def email_icon_preview(self, obj):
        if obj.email_icon:
            return format_html('<img src="{}" style="width: 40px; height:auto;" />', obj.email_icon.url)
        return "No Icon"
    email_icon_preview.short_description = "Email Icon"
