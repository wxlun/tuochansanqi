import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import client

class command_handler(object):
    def __init__(self,sys_args):
        self.sys_args = sys_args
        #至少传递一个参数的检测
        if len(self.sys_args)<2:
            exit(self.help_msg())
        self.command_allowcator()

    def command_allowcator(self):
        '''分拣用户输入的不同命令'''
        print(self.sys_args)

        if hasattr(self,self.sys_args[1]):
            func = getattr(self,self.sys_args[1])
            return func()
        else:
            print("command does not exist!")
            self.help_msg()

    def help_msg(self):
        valid_commands = '''
       start start monitor client
       stop  stop monitor client
       '''
        exit(valid_commands)

    def start(self):
        print("going to start the monitor client")
        # exit_flag = False
        Client = client.ClientHandle()
        Client.forever_run()

    def stop(self):
        print("stopping the monitor client")