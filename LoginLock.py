# coding:utf-8
import os
import time
import re
import datetime
import binascii

def loglock(username,clientaddr):
   
    t = time.time()
    nowdate=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    nowTime = lambda:int(round(t * 1000))

    filepath=os.getcwd()+"\\config\\"
    lock_file=filepath+"lock_file.txt"
    account_file=filepath+"account_file.txt"
    
    #print("打开lock_file文件")
    lock_read = open(lock_file,"r+")
    
    sign=0
    data=""
    for lock in lock_read:   
        if username in lock :
            sign=1    
            lock_num=lock.strip().split(",")[1]
            if (int(lock_num)+1)==3:#错误三次锁定
                #print("打开修改account_file文件")
                account_read=open(account_file, "r+")
                account_lines=account_read.readlines()
                num=0
                for line in account_lines:
                    #print("username:"+username+":"+line)
                    if (line.find(username)==0):
                        line=line.replace("Y","N")
                    data+=line
                    #print(data)
                    num+=1
                open(account_file, "r+").writelines(data)
            
            #密码错误记录
            #print("打开修改lock_file文件")
            #读取readlines
            lock_lines=open(lock_file,"r+").readlines()
            #lock_lines=lock_read.readlines()
            #print ("Read Line: %s" % (lock_lines))
            num=0
            #print("num:"+str(num))
            #print("lock_num:"+lock_num)
            data=""
            for line in lock_lines:
                #print("username:"+username+":"+line)
                if (line.find(username)==0):
                    line=line.replace(lock_num,str(int(lock_num)+1))
                data+=line
                #print(data)
                num+=1
            #写入readlines
            open(lock_file,"r+").writelines(data)       
            
    if sign==0:
        #print("新增lock_file文件")
        file_data=username+",1,"+str(nowdate)+","+str(nowTime())
        lock_write = open(filepath+"lock_file.txt","a+")
        #lock_write.write("\n")
        lock_write.write(file_data+"\n")
        lock_write.close()



    
