from django.shortcuts import render
from django.urls import reverse_lazy
from.forms import SignUpForm
from django.views import generic
from .models import Product_table

# Create your views here.
class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def upload_product(request):
    pass
