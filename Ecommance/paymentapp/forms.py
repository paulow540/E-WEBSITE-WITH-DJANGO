from django import forms
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Ecommance.paymentapp.models import Order_table
from django.apps import AppConfig

# class PaymentappConfig(App)

class AddToCart_form(forms.ModelForm):
    class Meta:
        model =Order_table
        fields =[
            'quantity'
        ]


class PaymentOption_form(forms.Form):
    CHOICES = [ ('mater_card', 'Master card'),
                ('visa_card', 'Visa card'),
                ('pay_delivery', 'Pay on delivery'),

    ]
    option = forms.ChoiceField(choices =CHOICES, widget = forms.RadioSelect)


class CardDetails_form(forms.Form):
    card_number = forms.CharField(max_length =20)
