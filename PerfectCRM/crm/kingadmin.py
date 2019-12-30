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
    filter_horizontal = ['consult_courses',]
    list_per_page = 5

    actions = ['change_status']
    def change_status(self,request,querysets):
        querysets.update(status=1)

site.register(models.CustomerInfo,CustomerAdmin)
site.register(models.Role)
site.register(models.Menus)
site.register(models.Course)
site.register(models.ClassList)
site.register(models.CourseRecord)
site.register(models.StudyRecord)
site.register(models.UserProfile)
site.register(models.Student)

