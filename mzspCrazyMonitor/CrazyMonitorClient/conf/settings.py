configs = {
    'HostID':1,
    'Server':'192.168.0.17',
    'ServerPort':8000,
    'urls':{
        'get_configs':['api/client/config/','get'],    #acquire all the services will be monitored
        'service_report':['api/client/service/report/','port'],
    },
    'RequestTimeout':30,
    'ConfigUpdateInterval':300, # 5 mins as defaults

}