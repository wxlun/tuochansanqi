#_*_coding:utf-8_*_
__author__ = 'wxlun'

configs = {
    'HostID':1,
    'Server':"192.168.0.17",
    "ServerPort":8000,
    "url":{
        'get_configs':['api/client/config','get'], #aquire all the services will be monitored
        'service_report':['api/client/config/service/report/','port'],
    },
    'RequestTimeout':30,
    'ConfigUpdateInterval':300, #5 mins as default
}

