from django.conf.urls import url
from Ecommance.adminapp import views as admin_view

urlpatterns = [
    url(r'^product_upload/$', admin_view.upload_product, name='upload_prod'),
]