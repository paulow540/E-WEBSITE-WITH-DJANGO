# Generated by Django 3.1.1 on 2021-10-13 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminapp', '0005_delete_order_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('nationality', models.CharField(choices=[('Nigeria', 'Nigeria'), ('Ghana', 'Ghana'), ('United Kingdom', 'UK'), ('USA', 'USA')], max_length=20, null=True)),
                ('state', models.CharField(choices=[('Abia', 'Abia'), ('Oyo', 'Oyo'), ('Osun', 'Osun'), ('Lagos', 'Lagos'), ('Kano', 'Kano'), ('Abuja', 'Abuja')], max_length=20, null=True)),
                ('means_of_identity', models.ImageField(null=True, upload_to='identityImage/')),
                ('particulars', models.FileField(null=True, upload_to='particularsImage/')),
                ('profile_passport', models.ImageField(null=True, upload_to='staffImage/')),
                ('position', models.CharField(choices=[('CEO', 'CEO'), ('GMD', 'GMD'), ('CTO', 'CTO'), ('HR', 'HR'), ('Staff', 'Staff'), ('Accountant', 'Accountant'), ('Marketer', 'Marketer')], max_length=20, null=True)),
                ('marital_status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorce', 'Divorce'), ('Complicate', 'Complicate')], max_length=12, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
