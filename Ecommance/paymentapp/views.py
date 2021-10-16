from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from Ecommance.adminapp.models import Product_table
from django.http import HttpResponseRedirect , HttpResponsePermanentRedirect 
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import AddToCart_form
from .models import Order_table, Invoice_table

# Create your views here.



price =0
@login_required
def addToCart(request, prod_id):
    global price
    if request.method == "POST":
        form =AddToCart_form(request.POST)
        if form.is_valid():
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

@login_required
def product_FromCart(request, prod_id):
    cart_details = Order_table.objects.filter(user_id = request.user.id)
    return render(request, "paymentapp/cart_product.html", {'product': cart_details})




@login_required   
def edit_Order(request, prod_id):
    global price
    edit = get_object_or_404(Order_table, product_id=prod_id)
    form =AddToCart_form(request.POST or None, request.FILES or None, instance=edit)
    if request.method == "POST":
        if (form.is_valid):
            form.save()
            details =Order_table.objects.get(product_id =prod_id)
            price = int(details.quantity) * int(price)
            Order_table.objects.filter(product)

    

@login_required
def delete_Order(request, order_id):
    Order_table.objects.filter(order_id =order_id).delete()
    return product_FromCart(request)
    
    
@login_required
def order_Receipt(request, user_id):
    order =Order_table.objects.filter(user_id =user_id)
    receipt = Invoice_table(order_id =order.id, product_id = order.product_id, date_cashout = timezone.now, user_id =user_id,
    total_price =order.price.sum())
    receipt.save()
    receipt_details =Invoice_table.objects.filter(user_id =user_id)
    return 0
    # return render(request, template_name = "paymentapp/receipt.html", context ={"receipt": receipt_details})