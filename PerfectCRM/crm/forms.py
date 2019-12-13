from django.forms import ModelForm
from crm import models

class CustomerForm(ModelForm):
    class Meta:
        models = models.CustomerInfo
        # fields = ['name','status']
        fields = "__all__"