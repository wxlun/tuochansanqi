from django.shortcuts import render
from django import forms
from django.forms import fields,widgets

class TestForm(forms.Form):
    user = fields.CharField(
        required=True,
        max_length=12,
        min_length=3,
        error_messages={},

    )
    age = fields.IntegerField()
    email = fields.EmailField()

def test(request):
    obj = TestForm()
    render(request,'test.html',{'obj':obj})