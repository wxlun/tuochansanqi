import paramiko

client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(hostname='192.168.24.94',port=22,username='root',password='oy@)!(DaFy37')
stdin,stdout,stderr = client.exec_command('df -h')
print(stdout.read().decode('utf-8'))

client.close()