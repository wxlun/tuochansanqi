#_*_coding:utf-8_*_
__author__ = 'wxlun'
from dbinfo.utils.sqlheper import SqlHelper
from dbinfo import models
import time



def forever_run():
    '''先手动触发，后改成自动采集'''
    time.sleep(86400)
    db_list= list(models.dbmysql.objects.values_list('ip','port').filter(role='查'))
    for db in db_list:
        obj = SqlHelper()
        obj.connect(db[0],db[1])
        sql = "select user,host from user;"
        result = obj.get_list(sql,[])
        obj.close()
        models.usercollection.objects.filter(ip=db[0],port=db[1]).delete()  #删除对应 ip + port 的用户
        for each in result: #插入对应 ip + port 的用户
            models.usercollection.objects.create(ip=db[0],port=int(db[1]),username=each['user'],hostname=each['host'])


    # def __init__(self):
    #     self.monitored_services = {}
    #
    # def load_latest_configs(self):
    #     '''
    #     load the latest monitor configs from monitor server
    #     :return:
    #     '''
    #     request_type = settings.configs['urls']['get_configs'][1]
    #     url = "%s/%s" %(settings.configs['urls']['get_configs'][0], settings.configs['HostID'])
    #     latest_configs = self.url_request(request_type,url)
    #     latest_configs = json.loads(latest_configs)
    #     self.monitored_services.update(latest_configs)
    #
    # def forever_run(self):
    #     '''
    #     start the client program forever
    #     :return:
    #     '''
    #     exit_flag = False
    #     config_last_update_time = 0
    #     while not exit_flag:
    #           if time.time() - config_last_update_time > settings.configs['ConfigUpdateInterval']:
    #               self.load_latest_configs()
    #               print("Loaded latest config:", self.monitored_services)
    #               config_last_update_time = time.time()
    #           #start to monitor services
    #
    #           for service_name,val in self.monitored_services['services'].items():
    #               if len(val) == 2:# means it's the first time to monitor
    #                   self.monitored_services['services'][service_name].append(0)
    #               monitor_interval = val[1]
    #               last_invoke_time = val[2]
    #               if time.time() - last_invoke_time > monitor_interval: #needs to run the plugin
    #                   print(last_invoke_time,time.time())
    #                   self.monitored_services['services'][service_name][2]= time.time()
    #                   #start a new thread to call each monitor plugin
    #                   t = threading.Thread(target=self.invoke_plugin,args=(service_name,val))
    #                   t.start()
    #                   print("Going to monitor [%s]" % service_name)
    #
    #               else:
    #                   print("Going to monitor [%s] in [%s] secs" % (service_name,
    #                                                                                  monitor_interval - (time.time()-last_invoke_time)))
    #
    #           time.sleep(1)
