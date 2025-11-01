from django.db import models
import time
import random


def generate_product_number():
    # 1970 tvich minchev hima qani ms e ancel ev inchvor randov tiv
    timestamp = int(time.time() * 1000)
    random_number = random.randint(1000, 9999)
    return f"{timestamp}-{random_number}"


def default_btn_text():
    return {
        "en": "ADD TO BAG",
        "ru": "ДОБАВИТЬ В КОРЗИНУ",
        "am": "ԱՎԵԼԱՑՆԵԼ ԶԱՄԲՅՈՒՂԻՆ"
    }


class Logo(models.Model):       
    image = models.FileField(upload_to='global/logo/')
    
    class Meta:
        verbose_name = "Logo"
        verbose_name_plural = "Logo"


class Category(models.Model):       
    lang = models.CharField(max_length=5)
    title = models.CharField(max_length=255)
    descr = models.CharField(max_length=255)
    image = models.FileField(upload_to='global/category/')
    category_name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
     


class Categories_link(models.Model):
    lang = models.CharField(max_length=5)
    main = models.CharField(max_length=100)
    catalog = models.CharField(max_length=100)
    filter_by = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    materials = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    sort_by = models.CharField(max_length=100)
    from_field = models.CharField(max_length=100) 
    to_field = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.lang} -> links"
       

class Item(models.Model):
    is_popular = models.BooleanField(default=False)
    is_new_arrival = models.BooleanField(default=False)
    category_name = models.CharField(max_length=100)
    product_number = models.CharField(max_length=255, unique=True, default=generate_product_number)
    price = models.FloatField()
    heart_icon = models.BooleanField(default=False)
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    group_code = models.CharField(max_length=255, blank=True, null=True)
    title = models.JSONField()
    btn_text = models.JSONField(default=default_btn_text)
    descr = models.JSONField()
    product_material = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"



class ItemAboutDelivery(models.Model):
    about_delivery = models.JSONField()
    
    def __str__(self):
        return "About delivery | О доставке | Առաքման մասին"
    
    class Meta:
        verbose_name = "Item About Deilivery"
        verbose_name_plural = "Items About Deilivery"



class ProductImage(models.Model):
    image = models.FileField(upload_to='global/items/')
    is_general = models.BooleanField(default=False)
    product = models.ForeignKey(Item, related_name="images", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Remove automatic setting of is_general
        # Let the admin interface handle it through radio buttons
        super().save(*args, **kwargs)




class ItemHeader(models.Model):
    lang = models.CharField(max_length=5)
    image = models.FileField(upload_to='global/items-header/')
    category_name = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=255)
    descr = models.CharField(max_length=255)
    

class ItemPageField(models.Model):
    lang = models.CharField(max_length=5)
    size_text_field = models.CharField(max_length=255)
    size_text_field_2 = models.CharField(max_length=255)
    descr_text_field = models.CharField(max_length=255)
    product_number_text_field = models.CharField(max_length=255)
    material_text_field = models.CharField(max_length=255)
    about_delivery_text_field = models.CharField(max_length=255)
    not_available_text_field = models.CharField(max_length=255)
        
    def __str__(self):
        return self.lang
    

class ItemLink(models.Model):
    lang = models.CharField(max_length=5)
    item = models.CharField(max_length=30)
    catalog = models.CharField(max_length=30)
    cribs = models.CharField(max_length=30)
    
    def __str__(self):
        return self.lang
  

class ItemFaqHeading(models.Model):
    lang = models.CharField(max_length=5)
    heading = models.CharField(max_length=255)
          
    def __str__(self):
        return self.heading
    
  
class ItemFaq(models.Model):
    lang = models.CharField(max_length=5)
    question = models.TextField()
    answer = models.TextField()
            
    def __str__(self):
        return self.question
    
   
class LikedProductHeading(models.Model):
    lang = models.CharField(max_length=5)
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
    

class InfoAboutDelivery(models.Model):
    lang = models.CharField(max_length=5)
    title = models.CharField(max_length=255)
    texts = models.JSONField()
        
    def __str__(self):
        return self.title


