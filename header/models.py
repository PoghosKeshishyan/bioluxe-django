from django.db import models


class Navbar(models.Model):
    lang = models.CharField(max_length=5)
    title = models.CharField(max_length=50)
    route = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.lang} -> {self.title}'


class Submenu(models.Model):
    navbar = models.ForeignKey(
        Navbar, 
        on_delete=models.CASCADE, 
        related_name='submenus'
    )
    
    lang = models.CharField(max_length=5)
    title = models.CharField(max_length=50)
    route = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class HeaderIcon(models.Model):
    search_icon = models.FileField(upload_to='header_icons/')
    heart_icon = models.FileField(upload_to='header_icons/')
    cart_icon = models.FileField(upload_to='header_icons/')
    language_arrow_icon = models.FileField(upload_to='header_icons/')
    created_at = models.DateTimeField(auto_now_add=True)
        
    class Meta:
        verbose_name = "icon"
        verbose_name_plural = "Icons"
    

class Language(models.Model):
    lang = models.CharField(max_length=5)
    label = models.CharField(max_length=20)
    image = models.FileField(upload_to='header_icons/')
    created_at = models.DateTimeField(auto_now_add=True)
    

class SavedHeartItem(models.Model):
    lang = models.CharField(max_length=5)
    heading = models.CharField(max_length=100)
    add_button_icon = models.CharField(max_length=5)
    add_button_text = models.CharField(max_length=100)
    remove_button_icon = models.CharField(max_length=5)
    remove_button_text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    
class SavedBasketItem(models.Model):
    lang = models.CharField(max_length=5)
    heading = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    remove_button_icon = models.CharField(max_length=5)
    remove_button_text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    

class BasketHeartViewLink(models.Model):
    lang = models.CharField(max_length=5)
    text = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text