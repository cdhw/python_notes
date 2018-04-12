#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
ret_text_list = os.popen("ps -ef | grep adi.jar")
pid_list = []
r = ret_text_list.readlines()
if len(r) > 1:
    for line in r:
        pid_list.append(line)
cmd_list = pid_list[0].split()
pid_num = cmd_list[1]
os.system("kill -9 %s" % pid_num)
os.popen("nohup java -jar adi.jar &")
