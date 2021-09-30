from django.shortcuts import get_object_or_404, render
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
    product_details = Product_table.objects.only('product_id','product_name','price','profile_picture').filter(status="approved")
    return render(request, 'index.html', {'product':product_details})


@login_required
def upload_product(request):
    if request.method == 'POST':
        form = Product_form(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user.id
            post.date_upload =timezone.now()
            post.status="unapprove"
            post.save()
            return HttpResponsePermanentRedirect(reverse('upload_prod'))
    else:
        form = Product_form()
        return render(request=request, template_name ='adminapp/upload_product_form.html',context={'form':form})



@login_required
def manage_product(request):
    product_details = Product_table.objects.all()
    return render(request, 'adminapp/manage_product.html',{'product':product_details })

@login_required
def approve_product(request, prod_id):
    product =Product_table.objects.get(product_id=prod_id)
    if product.status =="approved":        
        product.status ="unapprove" 
        
    else:
        product.status ="approved"    
    product.save()
    return manage_product(request)  

    

@login_required
def edit_product(request,prod_id):
    pass
    # edit= get_object_or_404(Product_table, prod_id)
    # form = Product_form (request.POST or None, request.FILES or None)



@login_required
def delete_product(request,prod_id):
    pass

    
@login_required
def product_description(request, prod_id):
    product_details = Product_table.object.get(product_id =prod_id)
    return render(request=request, template_name='admin/shop-single.html', context={'product':product_details})
