from django.conf.urls import url
from Ecommance.adminapp import views as admin_view

urlpatterns = [
    url(r'^product_upload/', admin_view.upload_product, name='upload_prod'),
    url(r'^product_description/(?P<user_id>\d+)/', admin_view.upload_product, name='upload_description'),    
    url(r'^manage_product/', admin_view.manage_product, name='manage_prod'),
    url(r'^user_profile/(?P<user_id>\d+)/', admin_view.manage_product, name='user_profile'),
    url(r'^product_status/(?P<prod_id>\d+)/', admin_view.approve_product, name='status_prod'),
    url(r'^edit_product/(?P<prod_id>\d+)/', admin_view.edit_product, name='edit_prod'),
    url(r'^delete_product/(?P<user_id>\d+)/', admin_view.delete_product, name='delete_prod'),
    ]