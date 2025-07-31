from django.db import models

# Create your models here.
class ProductModel(models.Model):
    product_name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    brand = models.CharField(max_length=100, null=True)
    price = models.CharField(max_length=100, null=True)
    register_date = models.DateField(auto_now_add=True, null=True)
    def __str__(self):
        return self.product_name