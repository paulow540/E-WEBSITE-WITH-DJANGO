from django.conf.urls import url
from django.apps import AppConfig
from Ecommance.paymentapp import views as payment_view




urlpatterns =[
    url(r'^product_description/(?P<user_id>\d+)/', payment_view.addToCart, name='user_profile'),    
    url(r'^carproduct/', payment_view.product_FromCart, name = 'cart_prod'),
    url(r'^product_description/(?P<prod_id>\d+)/', payment_view.edit_Order, name='order_edit'),    
    url(r'^carproduct/(?P<prod_id>\d+)/', payment_view.delete_Order, name = 'order_del'),
    url(r'^order_receipt/(?P<user_id>\d+)/', payment_view.order_Receipt, name = 'receipt'),
]