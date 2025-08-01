from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class customUserModel(AbstractUser):
    role = [
        ('customer', "Customer"),
        ('owner', "Owner")
    ]
    user_types = models.CharField(choices=role, max_length=100, null=True)
    profile_image = models.ImageField(upload_to='media/users', null=True)
    full_name = models.CharField(max_length=100, null=True)
    date_of_birth = models.DateField(null=True)


class productModel(models.Model):
    product_image = models.ImageField(upload_to='media/products', null=True)
    product_name =models.CharField(max_length=100, null=True)
    product_description =models.TextField()
    product_price =models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)