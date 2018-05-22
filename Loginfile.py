# coding:utf-8
import os
import time
import datetime
import binascii


def logfile(username,clientaddr):
    
    
    t = time.time()
    nowdate=datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')
    nowTime = lambda:int(round(t * 1000))
    tokenfile=binascii.b2a_base64(os.urandom(24))[:-1]
    tokenfile=str(tokenfile).replace("b'",'').replace("'",'')
    #print(tokenfile)
    filepath=os.getcwd()+"\\config\\"
    login_read = open(filepath+"login_file.txt","r")#读取权限
    
    loginlog=0
    nusum=0
    for login in login_read:
        if nusum==0:
            nusum+=1
            continue
        else:
            login_user = login.strip().split(",")[0]        #取出power文件里面的权限用户名
            tokenfile=login.strip().split(",")[3] #测试  正式注释掉
            login_ip=login.strip().split(",")[4]
            if username == login_user: 
                if clientaddr==login_ip:
                    loginlog=1
                    break
    
    if loginlog!=1:
        login_write = open(filepath+"login_file.txt","a+")
        login_write.write("\n")
        login_write.write(username+","+nowdate+","+str(nowTime())+","+str(tokenfile)+","+str(clientaddr))
        login_write.close()
        return tokenfile
    else:
        return tokenfile#""#tokenfile # 正式还成"" 空

    