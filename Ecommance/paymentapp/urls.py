from django.conf.urls import url
from django.apps import AppConfig
from Ecommance.paymentapp import views as payment_view


urlpatterns =[
    url(r'^product_description/(?P<user_id>\d+)/', payment_view.addToCart, name='prod_description'),    
    url(r'^carproduct/', payment_view.product_FromCart, name = 'cart_prod',)
]