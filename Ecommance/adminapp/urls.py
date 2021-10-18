from django.conf.urls import url
from Ecommance.adminapp import views as admin_view

urlpatterns = [
    url(r'^product_upload/', admin_view.upload_product, name='upload_prod'),
    url(r'^manage_upload/$', admin_view.manage_product, name='manage_prod'),
    url(r'^manage_staff/$', admin_view.manage_staff, name='manage_staff'),
    url(r'^staff_profile/(?P<user_id>\d+)/', admin_view.staff_profile, name='staff_profile'),
    url(r'^edit_profile/(?P<prod_id>\d+)/', admin_view.edit_profile, name='edit_profile'),       
    
    url(r'^user_profile/(?P<user_id>\d+)/', admin_view.manage_product, name='user_profile'),
    url(r'^product_status/(?P<prod_id>\d+)/', admin_view.approve_product, name='status_prod'),
    url(r'^edit_product/(?P<prod_id>\d+)/', admin_view.edit_product, name='edit_prod'),
    url(r'^delete_product/(?P<user_id>\d+)/', admin_view.delete_product, name='delete_prod'),
    url(r'^product_list/(?P<category>\D+)/', admin_view.product_full_list, name='list_prod'),    
    ]