from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import User, Group
from rest_framework.routers import DefaultRouter

from root.views import index
from header.views import (
    NavbarViewSet, SubmenuViewSet, HeaderIconViewSet,
    LanguageViewSet, SavedHeartItemViewSet, SavedBasketItemViewSet,
    BasketHeartViewLinkViewSet
)
from footer.views import FooterInfoViewSet, FooterSocialLinkViewSet, FooterPrivacyPolicyViewSet
from global_data.views import (
    LogoViewSet, CategoryViewSet, CategoriesLinkViewSet, ItemViewSet,
    ItemHeaderViewSet, ItemPageFieldViewSet,
    ItemLinkViewSet, ItemFaqHeadingViewSet, ItemFaqViewSet,
    LikedProductHeadingViewSet, InfoAboutDeliveryViewSet
)
from home_page.views import (
    SliderViewSet, SliderIconViewSet, AboutUsViewSet,
    PopularItemHeadingViewSet, PopularItemViewSet, 
    NewArrivalsHeadingViewSet, ContactUsViewSet, 
    CategoriesHeadingViewSet, PartnersHeadingViewSet, 
    PartnerViewSet
)
from about_page.views import AbouPageViewSet, AboutPageTextViewSet
from contact_page.views import ContactTitleViewSet, ContactInfoViewSet, ContactFormViewSet
from shopping_bag_page.views import ShopingBagPageViewSet


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


# ===================================
# API router
# ===================================

router = DefaultRouter()

# header
router.register(r"navbar", NavbarViewSet, basename="navbar")
router.register(r"header_icons", HeaderIconViewSet, basename="headericon")
router.register(r"languages", LanguageViewSet, basename="language")
router.register(r"saved_heart_items", SavedHeartItemViewSet, basename="savedheartitem")
router.register(r"saved_basket_items", SavedBasketItemViewSet, basename="savedbasketitem")
router.register(r"basket_heart_view_link", BasketHeartViewLinkViewSet, basename="basketheartviewlink")

# footer
router.register(r"footer_info", FooterInfoViewSet, basename="footerinfo")
router.register(r"footer_social_links", FooterSocialLinkViewSet, basename="footersociallink")
router.register(r"footer_privacy_policy", FooterPrivacyPolicyViewSet, basename="footerprivacypolicy")

# global 
router.register(r"logo", LogoViewSet, basename="global-logo")
router.register(r"categories", CategoryViewSet, basename="global-categories")
router.register(r"categories_link", CategoriesLinkViewSet, basename="global-categories-links")
router.register(r"items", ItemViewSet, basename="global-items")
router.register(r"popular/items", PopularItemViewSet, basename="popular-items")
router.register(r"items_header", ItemHeaderViewSet, basename="global-item-headers")
router.register(r"item_page_fields", ItemPageFieldViewSet, basename="global-item-page-fields")
router.register(r"item_link", ItemLinkViewSet, basename="global-item-links")
router.register(r"item_faq_heading", ItemFaqHeadingViewSet, basename="global-item-faq-headings")
router.register(r"item_faq", ItemFaqViewSet, basename="global-item-faqs")
router.register(r"liked_product_heading", LikedProductHeadingViewSet, basename="global-liked-product-headings")
router.register(r"infoAbout_delivery", InfoAboutDeliveryViewSet, basename="global-info-about-delivery")

# home-page
router.register(r"slider", SliderViewSet, basename="home-sliders")
router.register(r"slider_icons", SliderIconViewSet, basename="home-slider-icons")
router.register(r"categories_heading", CategoriesHeadingViewSet, basename="home-categories-headings")
router.register(r"homepage_about_us", AboutUsViewSet, basename="home-about-us")
router.register(r"homepage_popular_items_heading", PopularItemHeadingViewSet, basename="home-popular-item-headings")
router.register(r"homepage_new_arrivals_heading", NewArrivalsHeadingViewSet, basename="home-new-arrivals-headings")
router.register(r"homepage_contacts", ContactUsViewSet, basename="home-contact-us")
router.register(r"homepage_partners_heading", PartnersHeadingViewSet, basename="home-partners-headings")
router.register(r"homepage_partners", PartnerViewSet, basename="home-partners")


# about-page
router.register(r'about_us', AbouPageViewSet, basename='aboutus')
router.register(r'about_texts', AboutPageTextViewSet, basename='abouttext')

# contact-page
router.register(r"contact_title", ContactTitleViewSet, basename="contacttitle")
router.register(r"contact_info", ContactInfoViewSet, basename="contactinfo")
router.register(r"contact_form", ContactFormViewSet, basename="contactform")


# shopping-bag-page
router.register(r"shopping_bag_page", ShopingBagPageViewSet, basename="shopping-bag-page")


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
