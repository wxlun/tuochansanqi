"""wxlundjangotest01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from wxlundjangotest import viewsbak
from wxlundjangotest.views import mysqlcfg

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^dbinfoselect', viewsbak.dbinfoselect),
    url('^index', mysqlcfg.index),
    url('^login', viewsbak.login),
    url('^add_dbinfo', viewsbak.add_dbinfo),
    url('^get_mysqlinfo', mysqlcfg.get_mysqlinfo),
    url('^add_mysql', mysqlcfg.add_mysql),
    url('^del_mysql', mysqlcfg.del_mysql),
    url('^edit_mysql', mysqlcfg.edit_mysql),

]
