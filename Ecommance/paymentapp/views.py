from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from Ecommance.adminapp.models import Product_table
from django.http import HttpResponseRedirect , HttpResponsePermanentRedirect 
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import AddToCart_form
from .models import Order_table

# Create your views here.



price =0
@login_required
def addToCart(request, prod_id):
    global price
    if request.method == "POST":
        form =AddToCart_form(request.POST)
        if foem.is_valid():
            quantity = form.cleaned_data["quantity"]
            total_price = int(quantity) * int(price)
        post = Order_table(price =total_price, quantity =quantity)
        post.user_id =request.user.id
        post.data_upload =timezone.now()
        post.product_id = prod_id
        post.save()
        return HttpResponsePermanentRedirect(reverse('cart_prod'))
    
    else:
        form =AddToCart_form()
        product_details = Product_table.object.get(product_id =prod_id)
        price =product_details.price
        content = {'form':form, "product":product_details}
        return render(request=request, template_name='shop-single.html',context={'form':form ,'product':product_details})


def product_FromCart():
    pass

