#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: shut
# @time: 2018/4/2 17:16
#!/usr/bin/python

import os,re,sys, subprocess


def kill_by_name(name):
    cmd='ps aux|grep %s'%name
    f=subprocess.Popen(cmd)
    regex=re.compile(r'/w+/s+(/d+)/s+.*')
    txt=f.read()
    if len(txt)<5:
        print('there is no thread by name or command %s'%name)
        return

    ids=regex.findall(txt)
    cmd="kill %s"%' '.join(ids)
    os.system(cmd)


if __name__=='__main__':
    if len(sys.argv)==1:
        name=input("type the process command name:")
    else:
        name=sys.argv[1]
    kill_by_name(name)