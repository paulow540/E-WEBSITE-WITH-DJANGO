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
from Ecommance.adminapp.views import SignUpView
from Ecommance.userapp.views import userProfile as user_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TemplateView.as_view(template_name="index.html"), name ="homepage"),
    path("contact/", TemplateView.as_view(template_name="contact.html"), name = "contact"),
    path("about/", TemplateView.as_view(template_name="about.html"), name = "about"),
    path("shop/", TemplateView.as_view(template_name="shop.html"), name = "shop"),
    path("shop-single/", TemplateView.as_view(template_name="shop-single.html"), name = "shop-single"),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/signup/$', SignUpView.as_view(), name ="signup")
    url(r'^username/(?P<user_id>\d+)/', user_view.userProfile, name ="username")

]
