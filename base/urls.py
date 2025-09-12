from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import User, Group

admin.site.site_header = 'BIO LUXE'
admin.site.index_title = 'Welcome to Bio Luxe Admin panel'
admin.site.unregister(User)
admin.site.unregister(Group)

# ====================================
# App ordering function
# ====================================

DESIRED_APP_ORDER = ['header', 'footer', 'global_data', 'home_page', 'about_page', 'contact_page', 'shopping_bag_page']

class OrderedAdminSite(admin.AdminSite):
    def get_app_list(self, request, app_label=None):
        if app_label:
            return super().get_app_list(request, app_label)

        app_list = super().get_app_list(request)
        app_map = {app['app_label']: app for app in app_list}
        ordered = []

        for label in DESIRED_APP_ORDER:
            if label in app_map:
                ordered.append(app_map[label])

        for app in app_list:
            if app['app_label'] not in DESIRED_APP_ORDER:
                ordered.append(app)
                
        return ordered

admin.site.__class__ = OrderedAdminSite


urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
