from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(['GET', 'PUT', 'DELETE','POST'])
def index(request):
    print(request.method)
    print (request.DATA)
    return Response([{'asset': '1','request_hostname': 'c1.puppet.com' }])

