from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from.forms import SignUpForm ,Product_form
from django.views import generic
from .models import Product_table
from django.http import HttpResponseRedirect , HttpResponsePermanentRedirect 
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


@login_required
def upload_product(request):
    if request.method == 'POST':
        form = Product_form(request.POST, request.FILES)
        if form.is.valid():
            post = form.save(commit=False)



@login_required
def manage_product(request):
    product_details = Product_table.objects.all()
    return render(request, 'adminapp/manage_product.html')
    
