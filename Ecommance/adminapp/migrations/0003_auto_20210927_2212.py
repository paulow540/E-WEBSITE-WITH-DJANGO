# Generated by Django 3.1.1 on 2021-09-27 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_auto_20210915_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_table',
            name='category',
            field=models.CharField(choices=[('Wears', 'Wears'), ('Watch', 'Watch'), ('Electronics', 'Electronics'), ('Shoes', 'Shoes')], default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='product_table',
            name='display_type',
            field=models.CharField(choices=[('Fearure product', 'Fearure product'), ('Category product', 'Category product'), ('None', 'None')], default=None, max_length=20),
        ),
    ]
