from django.shortcuts import render,HttpResponse

from monitor.serializer import ClientHandler
import json

def client_configs(request,client_id):
    config_obj = ClientHandler(client_id)
    config = config_obj.fetch_configs()
    if config:
        return HttpResponse(json.dumps(config))
