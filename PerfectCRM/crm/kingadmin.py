from kingadmin.sites import site
from kingadmin.admin_base import BaseKingAdmin
from crm import models

# print('crm kingamdin ....................')

class CustomerAdmin(BaseKingAdmin):
    list_display = ['id','name','source','contact_type','contact','consultant','consult_content','status','date']
    list_filter = ['source','consultant','status','date']
    # list_filter = ['source','consultant','status']

    search_fields = ['name','contact','consultant__name']
    readonly_fields = ['status','contact']

site.register(models.CustomerInfo,CustomerAdmin)
site.register(models.Role)
site.register(models.Course)
site.register(models.ClassList)
site.register(models.CourseRecord)