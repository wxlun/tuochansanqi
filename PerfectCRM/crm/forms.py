from django.forms import ModelForm
from crm import models

class EnrollmentForm(ModelForm):
    def __new__(cls,*args,**kwargs):
        for field_name in cls.base_fields:
            filed_obj = cls.base_fields[field_name]
            filed_obj.widget.attrs.update({'class':'form-control'})
            if field_name in cls.Meta.readonly_fields:
                filed_obj.widget.attrs.update({'disabled':'true'})

        return ModelForm.__new__(cls)
    class Meta:
        model = models.StudentEnrollment
        # fields = ['name','status']
        fields = "__all__"
        exclude = ['contract_approved_date']
        readonly_fields = ['contact_agreed']

class CustomerForm(ModelForm):
    def __new__(cls,*args,**kwargs):
        for field_name in cls.base_fields:
            filed_obj = cls.base_fields[field_name]
            filed_obj.widget.attrs.update({'class':'form-control'})
            if field_name in cls.Meta.readonly_fields:
                filed_obj.widget.attrs.update({'disabled':'true'})

        return ModelForm.__new__(cls)


    class Meta:
        model = models.CustomerInfo
        # fields = ['name','status']
        fields = "__all__"
        exclude = ['consult_content','status','consult_courses']
        readonly_fields = ['contact_type','contact','consultant','referral_from','source']