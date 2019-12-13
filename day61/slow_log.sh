#!/bin/bash
#host_ip=`/sbin/ifconfig -a|grep inet|grep -v 127.0.0.1|grep -v inet6|awk '{print $2}'|tr -d "addr:"|awk BEGIN{RS=EOF}'{gsub(/\n/,",");print}'`
host_ip=`/sbin/ifconfig -a|grep inet|grep -v 127.0.0.1|grep 192.168|grep -v inet6|awk '{print $2}'|tr -d "addr:"|awk BEGIN{RS=EOF}'{gsub(/\n/,",");print}'`
mysql_port=`netstat -lntup|grep -w mysqld|awk '{print $4}' | awk -F ':' '{print $NF}'`
mysql_user=root
mysql_passwd=jin2012cin
remote_ip=192.168.253.173
for port in $mysql_port
    do
        if [[ $port -eq 3306 ]];
            then
            logdir=/data/mysql/log/slow;

        else
            logdir=/data/mysql${port}/log/slow

        fi
        echo '------------- '`date +%Y-%m-%d' '%H:%M:%S`' 慢查询日志变更日期 -------------' >> $logdir/changelog.log
        /usr/local/mysql/bin/mysql -u${mysql_user} -p${mysql_passwd} -h${host_ip} -P${port} -N -e "
            show variables like 'slow_query_log_file';
            set global slow_query_log_file='$logdir/slow_${port}_$(date +%Y_%m_%d).log';
            show variables like 'slow_query_log_file';"
        >> ${logdir}/changelog.log
    done



for port in $mysql_port
    do
        if [[ $port -eq 3306 ]];
            then
            logdir=/data/mysql/log/slow;

        else
            logdir=/data/mysql${port}/log/slow

        fi
        echo '------------- '`date +%Y-%m-%d' '%H:%M:%S`'  拷贝到天兔 -------------' >> $logdir/changelog.log
        scp -P52208 $logdir/slow_${port}_$(date +%Y_%m_%d).log ${remote_ip}:/u01/wxlun/${host_ip}
    done
