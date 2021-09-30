from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Product_table(models.Model):
    cat =(
        ('Wears','Wears'),
        ('Watch','Watch'),
        ('Electronics','Electronics'),
        ('Shoes','Shoes')
    )
    d_type =(
        ("Feature product", "Feature product"),
        ("Category product", "Category product"),
        ("None", "None")
    )

    product_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name =models.CharField(unique=True, max_length=50)
    date_upload =models.DateTimeField(default=timezone.now)
    quantity = models.IntegerField(unique=False)
    price =models.IntegerField(unique=False)
    description = models.CharField(unique=False, max_length = 100, null=True)
    profile_picture = models.ImageField(upload_to='productImage/',unique=True)
    status= models.CharField(unique=False, max_length=10, null=True)
    category = models.CharField(max_length=20, choices=cat, default=None)
    display_type = models.CharField(unique=False, max_length=20, choices=d_type,default =None)
    