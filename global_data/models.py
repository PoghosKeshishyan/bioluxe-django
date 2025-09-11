from django.db import models


class Logo(models.Model):
    image = models.FileField(upload_to='global/logo/')


class Category(models.Model):
    lang = models.CharField(max_length=5)
    title = models.CharField(max_length=255)
    descr = models.CharField(max_length=255)
    image = models.FileField(upload_to='global/category/')
    category_name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

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


class ProductImage(models.Model):
    image = models.FileField(upload_to='global/items/')
    product = models.ForeignKey(Item, related_name="images", on_delete=models.CASCADE)
