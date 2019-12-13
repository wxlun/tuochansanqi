from django.forms import ModelForm

def create_dynamic_model_form(admin_class):
    """动态的生产modelform"""

    class Meta:
        model = admin_class.model
        fields = "__all__"

    def __new__(cls,*args,**kwargs):
        for field_name in cls.base_fields:
            filed_obj = cls.base_fields[field_name]
            filed_obj.widget.attrs.update({'class':'form-control'})
            if field_name in admin_class.readonly_fields:
                filed_obj.widget.attrs.update({'disabled':'true'})
        return ModelForm.__new__(cls)

    dynamic_form = type("DynamicModelForm",(ModelForm,),{'Meta':Meta,'__new__':__new__})

    return dynamic_form