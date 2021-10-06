from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from Ecommance.adminapp.models import Product_table

# Create your models here.


class Order_table(models.Model):
    order_id =models.AutoField(primary_key=True)
    date_purchased =models.DateTimeField(default=timezone.now)
    product =models.ForeignKey(Product_table, on_delete =models.CASCADE)
    user =models.ForeignKey(User, on_delete =models.CASCADE)
    quantity = models.IntegerField(unique=False)
    price = models.CharField(unique=False, max_length=11)
    purchased =models.BooleanField(default=False, unique =False)
    delivered =models.BooleanField(default=False, unique =False)
