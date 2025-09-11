from django.db import models


class FooterInfo(models.Model):
    lang = models.CharField(max_length=5)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    address_icon = models.FileField(upload_to='footer/')
    phone_icon = models.FileField(upload_to='footer/')
    email_icon = models.FileField(upload_to='footer/')
    created_at = models.DateTimeField(auto_now_add=True)
    

class FooterSocialLink(models.Model):
    icon = models.FileField(upload_to='footer/')
    url = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    

class FooterPrivacyPolicy(models.Model):
    lang = models.CharField(max_length=5)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    