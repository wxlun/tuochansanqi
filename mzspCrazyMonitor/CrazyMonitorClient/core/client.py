import time
import json

#python3 urllib 和 urllib2 合并为urllib
import urllib
from urllib import request

from conf import settings

class ClientHandle(object):
    def __init__(self):
        self.monitored_services = {}


    def load_latest_config(self):
        '''
        load the latest monitor configs from monitor server
        :return:
        '''
        request_type = settings.configs['urls']['get_configs'][1]
        url = "%s%s" %(settings.configs["urls"]['get_configs'][0],settings.configs['HostID'])
        latest_configs = self.url_request(request_type,url)
        latest_configs = json.loads(latest_configs)
        self.monitored_services.update(latest_configs)

    def forever_run(self):
        '''
        start the client progrem forever
        :return:
        '''
        exit_flag = False
        config_last_update_time = 0
        while not exit_flag:
            if time.time() - config_last_update_time > settings.configs['ConfigUpdateInterval']:
                self.load_latest_config()
                print("Loaded latest config:",self.monitored_services)
                config_last_update_time = time.time()

            #start to monitor services  未完成，所学视频也只是到这儿，而且有点bug，每5分钟取配置，把当前的配置覆盖
            for service_name,val in self.monitored_services['services'].items():
                if len(val) == 2: #means it's the first time to monitor
                    self.monitored_services['services'][service_name].append(0)
                monitor_interval = val[1]
                last_invoke_time = val[2]
                comp_time = monitor_interval - (time.time() - last_invoke_time)
                if time.time() - last_invoke_time > monitor_interval:
                    self.monitored_services['services'][service_name][2] = time.time()
                    print("Going to monitor [%s]" %service_name)

                else:
                    print('12343445545')


                    print("\033[34;1mGoing to monitor [%s] in [%s] secs \033;0m" %(
                        service_name,monitor_interval-(time.time()-last_invoke_time),
                    ))




            time.sleep(1)

    def url_request(self,action,url,**extra_data):
        '''
        cope with monitor server by url
        :param action: "get" or "post"
        :param url: whitch url you want to request from the monitor server
        :param extra_data: extra parameters needed to be submited
        :return:
        '''
        abs_url = "http://%s:%s/%s" %(settings.configs['Server'],
                                   settings.configs['ServerPort'],
                                   url)

        if action in ('get','GET'):
            print(abs_url,extra_data)
            try:
                req = urllib.request.Request(abs_url)
                req_date = urllib.request.urlopen(req,timeout = settings.configs['RequestTimeout'])
                callback = req_date.read()
                print('--> server response:',callback)
                return callback
            except urllib.request.URLError as e:
                exit("\033[31;1m%s\033[0m"%e)

