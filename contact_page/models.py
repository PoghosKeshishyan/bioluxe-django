from django.db import models


class ContactTitle(models.Model):
    lang = models.CharField(max_length=5)
    title = models.CharField(max_length=100)
    image_url = models.FileField(upload_to='contact-page/')
    

class ContactInfo(models.Model):
    lang = models.CharField(max_length=5)
    map_image = models.TextField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    address_icon = models.FileField(upload_to='contact-page/')
    phone_icon = models.FileField(upload_to='contact-page/')
    email_icon = models.FileField(upload_to='contact-page/')
    
    
class ContactForm(models.Model):
    lang = models.CharField(max_length=5)
    title = models.CharField(max_length=100)
    input_placeholder_name = models.CharField(max_length=30)
    input_placeholder_email = models.CharField(max_length=30)
    input_placeholder_phone = models.CharField(max_length=30)
    btn_text = models.CharField(max_length=30)
    priacy_policy_text = models.CharField(max_length=100)
    priacy_policy_url = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title