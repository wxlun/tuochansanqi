from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from monitor import api_urls
from monitor import views

urlpatterns = [
    url(r'^client/config/(\d+)/$',views.client_configs),
]
