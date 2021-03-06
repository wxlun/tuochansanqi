from django.contrib import admin
from monitor import models

class HostAdmin(admin.ModelAdmin):
    list_display = ('id','ip_addr','status')

admin.site.register(models.ServiceIndex)
admin.site.register(models.Service)
admin.site.register(models.Template)
admin.site.register(models.Trigger)
admin.site.register(models.Host,HostAdmin)
admin.site.register(models.HostGroup)
admin.site.register(models.Action)
admin.site.register(models.ActionOperation)
admin.site.register(models.Maintenance)

