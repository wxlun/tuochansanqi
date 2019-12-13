from django.conf.urls import  include, url
from django.contrib import admin
from rest_framework import routers
from cmdbtest01 import api
from cmdbtest01 import views


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', api.UserViewSet)
router.register(r'blogs', api.BLogViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'index/', views.index),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
