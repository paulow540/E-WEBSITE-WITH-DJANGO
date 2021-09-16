from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Ecommance.adminapp.models import Product_table

class   SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required="false", help_text ='Optional')
    last_name = forms.CharField(max_length=30, required="false", help_text ='Optional')
    email = forms.EmailField(max_length=30, required="false", help_text ='Enter a valid email address ')

class Meta:
    model =User
    fields =[
        'username',
        'first_name',
        'last_name',
        'email',
        'password1',
        'password2'
        
    ]


class Product_form(forms.ModelForm):
    class Meta:
        model = Product_table
        fields =[
            'product_name',
            'price',
            'quantity',
            'description',
            'profile_picture',
        
    ]
    widgets ={
        'description':forms.Textarea(attrs={'cols':100,'rows':10})
    }
    


