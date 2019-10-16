from django.contrib import admin
from app01.models import *
# Register your models here.

# @admin.register(Book)#----->单给某个表加一个定制
# class MyAdmin(admin.ModelAdmin):
#     list_display = ("title","price","publisher")
#     search_fields = ("title","publisher")
#     list_filter = ("publisher",)
#     ordering = ("price",)
#     fieldsets =[
#         (None,               {'fields': ['title']}),
#         ('price information', {'fields': ['price',"publisher"], 'classes': ['collapse']}),
#     ]

class MyAdmin(admin.ModelAdmin):
    list_display = ("name","price","publish")
    search_fields = ("name",)
    list_filter = ("pub_date","name")
    ordering = ("price",)

admin.site.register(Book,MyAdmin)
admin.site.register(Publish)
admin.site.register(Author)