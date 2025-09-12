from django.db import models


class AboutUs(models.Model):
    lang = models.CharField(max_length=5)
    heading = models.CharField(max_length=100)
    image = models.FileField(upload_to='about-us/')

    class Meta:
        verbose_name_plural = 'About us'


class AboutText(models.Model):
    lang = models.CharField(max_length=5)
    heading = models.CharField(max_length=100)
    content1 = models.TextField()
    content2 = models.TextField()
    image = models.FileField(upload_to='about-us/')