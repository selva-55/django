from django.db import models

# Create your models here.
class products_details(models.Model):
    shop_name = models.CharField(max_length=40)
    product_name = models.CharField(max_length=40)
    product_price = models.IntegerField(max_length=10)
    product_quantity = models.CharField(max_length=10)
