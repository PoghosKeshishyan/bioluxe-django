from django.contrib import admin
from django.contrib.auth.models import User, Group

admin.site.site_header = 'BIO LUXE'
admin.site.index_title = 'Welcome to Bio Luxe Admin panel'

admin.site.unregister(User)
admin.site.unregister(Group)


# ====================================
# App ordering function
# ====================================

DESIRED_APP_ORDER = ['header', 'footer', 'global_data']

class OrderedAdminSite(admin.AdminSite):
    def get_app_list(self, request):
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