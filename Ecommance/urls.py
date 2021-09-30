"""Ecommance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic import TemplateView
from Ecommance.adminapp import views as admin_view
from Ecommance.userapp import views as user_view
from . import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", admin_view.index_page, name ="homepage"),
    path("contact/", TemplateView.as_view(template_name="contact.html"), name = "contact"),
    path("about/", TemplateView.as_view(template_name="about.html"), name = "about"),
    path("shop/", TemplateView.as_view(template_name="shop.html"), name = "shop"),
    path("shop-single/", TemplateView.as_view(template_name="shop-single.html"), name = "shop-single"),
    path("cart/", TemplateView.as_view(template_name="cart.html"), name = "cart"),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/ signup/$', admin_view.SignUpView.as_view(), name ="signup"),
    url(r'^adminapp/', include('Ecommance.adminapp.urls')),
    url(r'^username/(?P<user_id>\d+)/', user_view.userProfile, name ="username")

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)