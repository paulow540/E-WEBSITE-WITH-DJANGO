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


def index_page(request):
    pass
    # product_details = Product_table.object.only('product_id','product_name','price','profile_picture').filter(status="approved")
    # return render(request, 'index.html', {'product':product_details})






@login_required
def upload_product(request):
    if request.method == 'POST':
        form = Product_form(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user.id
            post.date_upload =timezone.Product_nameProduct_nameow()
            post.status="Unapprove"
            post.save()
            return HttpResponsePermanentRedirect(reverse('Upload_Product'))
    else:
        form = Product_form()
        return render(request=request, template_name ='adminapp/upload_product')



@login_required
def manage_product(request):
    product_details = Product_table.objects.all()
    return render(request, 'adminapp/manage_product.html', {'product':product_details})

@login_required
def approve_product(request, prod_id):
    # product
    pass





@login_required
def edit_product(request,prod_id):
    pass



@login_required
def delete_product(request,prod_id):
    pass

    
@login_required
def product_description(request, prod_id):
    product_details = Product_table.object.get(product_id =prod_id)
    return render(request=request, template_name='admin/shop-single.html', context={'product':product_details})
