from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Product_table(models.Model):
    product_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name =models.CharField(unique=True, max_length=50)
    date_upload =models.DateTimeField(default=timezone.now)
    quantity = models.IntegerField(unique=False)
    price =models.IntegerField(unique=False)
    description =models.CharField(unique=False, max_length = 100, null=True)
    profile_picture = models.ImageField(upload_to='productImage/',unique=True)
    status=models.CharField(unique=False, max_length=10, null=True)
    