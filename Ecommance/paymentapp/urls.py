from django.conf.urls import url
from django.apps import AppConfig
from Ecommance.paymentapp import views as payment_view




urlpatterns =[
    url(r'^product_description/(?P<prod_id>\d+)/', payment_view.addToCart, name='user_profile'),    
    url(r'^carproduct/', payment_view.product_FromCart, name = 'cart_prod'),
    url(r'^edit_order/(?P<prod_id>\d+)/', payment_view.edit_Order, name='order_edit'),    
    url(r'^delete_order/(?P<prod_id>\d+)/', payment_view.delete_Order, name = 'order_del'),
    url(r'^order_receipt/(?P<user_id>\d+)/', payment_view.order_Receipt, name = 'receipt'),
    url(r'^pay_service/(?P<user_id>\d+)/', payment_view.payment_service, name = 'pay_service'),
    url(r'^cancle_order/(?P<user_id>\d+)/', payment_view.cancle_order, name = 'cancle_order'),
    url(r'^card_detail/(?P<user_id>\d+)/', payment_view.card_detail, name = 'card_detail'),
    
    
]