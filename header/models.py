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
    

class Language(models.Model):
    lang = models.CharField(max_length=5)
    label = models.CharField(max_length=20)
    image = models.FileField(upload_to='header_icons/')
    created_at = models.DateTimeField(auto_now_add=True)