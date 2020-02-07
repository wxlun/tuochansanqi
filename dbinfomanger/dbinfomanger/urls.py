"""dbinfomanger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

from dbinfo import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login.html$', views.login),
    url(r'^index.html$', views.index),
    url(r'^mysql_cls.html$', views.mysql_cls),
    url(r'^mysql_info.html$', views.mysql_info),
    url(r'^collection/', include("dbinfo.collection.collection_urls")),
    url(r'^usermgr.html$', views.usermgr),
    url(r'^userauth.html$', views.userauth),

]
