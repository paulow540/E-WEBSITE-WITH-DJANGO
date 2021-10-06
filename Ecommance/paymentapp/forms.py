from django import forms
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Ecommance.paymentapp.models import Order_table
from django.apps import AppConfig



class AddToCart_form(forms.ModelForm):
    class Meta:
        model =Order_table
        fields =[
            'quantity'
        ]
