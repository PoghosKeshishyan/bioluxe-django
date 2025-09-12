from django.contrib import admin
from django.utils.html import format_html
from .models import FooterInfo, FooterSocialLink, FooterPrivacyPolicy


@admin.register(FooterInfo)
class FooterInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'lang', 'address', 'phone', 'email', 'address_display', 'phone_display', 'email_display')
    ordering = ('created_at',)

    def _preview(self, obj, field_name):
        file = getattr(obj, field_name)
        if file:
            return format_html('<img src="{}" width="20" />', file.url)
        return "-"

    def address_display(self, obj):
        return self._preview(obj, 'address_icon')
    address_display.short_description = 'Address Icon'

    def phone_display(self, obj):
        return self._preview(obj, 'phone_icon')
    phone_display.short_description = 'Phone Icon'

    def email_display(self, obj):
        return self._preview(obj, 'email_icon')
    email_display.short_description = 'Email Icon'
    

@admin.register(FooterSocialLink)
class FooterSocialLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'icon_display', 'url')
    ordering = ('created_at',)

    def _preview(self, obj, field_name):
        file = getattr(obj, field_name)
        if file:
            return format_html('<img src="{}" width="50" />', file.url)
        return "-"

    def icon_display(self, obj):
        return self._preview(obj, 'icon')
    icon_display.short_description = 'Icon'
    
    
@admin.register(FooterPrivacyPolicy)
class FooterPrivacyPolicyAdmin(admin.ModelAdmin):
    list_display = ('id', 'lang', 'title', 'url')
    list_filter = ('lang',)
    ordering = ('created_at',)
    