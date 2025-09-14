from django.db import models

class Slider(models.Model):
    lang = models.CharField(max_length=5)
    title = models.CharField(max_length=100)
    descr = models.CharField(max_length=255)
    btn_text = models.CharField(max_length=20)
    btn_url = models.CharField(max_length=20)
    background_image = models.FileField(upload_to='home-page/')
    image = models.FileField(upload_to='home-page/slider/')
    created_at = models.DateTimeField(auto_now_add=True)
    

class SliderIcon(models.Model):
    cloud_icon = models.FileField(upload_to='home-page/slider')
    left_arrow_icon = models.FileField(upload_to='home-page/slider')
    right_arrow_icon = models.FileField(upload_to='home-page/slider')
    

class AboutUs(models.Model):
    lang = models.CharField(max_length=5)
    heading = models.CharField(max_length=100)
    descr = models.TextField()
    btn_text = models.CharField(max_length=50)
    btn_url = models.CharField(max_length=50)
    image_1 = models.FileField(upload_to='home-page/about')
    image_2 = models.FileField(upload_to='home-page/about')
    
    class Meta:
        verbose_name_plural = "About us"
    

class PopularItemHeading(models.Model):
    lang = models.CharField(max_length=5)
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
    
class NewArrivalsHeading(models.Model):
    lang = models.CharField(max_length=5)
    title = models.CharField(max_length=100)
        
    def __str__(self):
        return self.title
    

class ContactUs(models.Model):
    lang = models.CharField(max_length=5)
    heading = models.CharField(max_length=100)
    map_image = models.FileField(upload_to='home-page/contact')
    map_url = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = "Contact us"
    

class CategoriesHeading(models.Model):
    lang = models.CharField(max_length=5)
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    

class PartnersHeading(models.Model):
    lang = models.CharField(max_length=5)
    heading = models.CharField(max_length=100)
    
    def __str__(self):
        return self.heading


class Partner(models.Model):
    image = models.FileField(upload_to='home-page/partners')
    