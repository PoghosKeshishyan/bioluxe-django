from django.db import models


class ShopingBagPage(models.Model):
    lang = models.CharField(max_length=5)
    main = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    empty_error_text = models.CharField(max_length=50)
    quantity_and_prais_text = models.CharField(max_length=50)
    size_title = models.CharField(max_length=50)
    heart_text = models.CharField(max_length=50)
    btn_text = models.CharField(max_length=50)
    order_summary_field = models.CharField(max_length=50)
    total_text_field = models.CharField(max_length=50)
    form_input_name_placeholder = models.CharField(max_length=50)
    form_input_tel_placeholder = models.CharField(max_length=50)
    form_input_address_placeholder = models.CharField(max_length=50)
    form_input_checkbox_text = models.CharField(max_length=50)
    form_btn_text = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Shopping bag page data'
        verbose_name_plural = 'Shopping bag page data'