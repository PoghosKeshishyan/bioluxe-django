from django.db import models


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
    category_name = models.CharField(max_length=100)
    product_number = models.CharField(max_length=255, unique=True)
    price = models.FloatField()
    heart_icon = models.BooleanField(default=False)
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    group_code = models.CharField(max_length=255, blank=True, null=True)
    title = models.JSONField()
    btn_text = models.JSONField()
    descr = models.JSONField()
    product_material = models.JSONField()
    about_delivery = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"


class ProductImage(models.Model):
    image = models.FileField(upload_to='global/items/')
    product = models.ForeignKey(Item, related_name="images", on_delete=models.CASCADE)


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
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
            
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
