# coding:utf-8
import json
from flask import Flask
from flask import make_response
from flask import jsonify
from flask import Request
from flask import request
from flask_cors import CORS
import ReturnFile as re
import Loginfile as log
import LoginLock as logk
import binascii
import os

def postLogin(filed,clientaddr):  
    # 定义文件请求的类型和当前请求成功的code
    #start_response('200 OK', [('Content-Type', 'application/json')])
    
    # environ是当前请求的所有数据，包括Header和URL，body
    
    

    username=str(filed['Name']).upper()
    password=filed['Password']
    typefile=filed['Type']
    
    filepath=os.getcwd()+"\\config\\"

    #print(filepath)
    with  open(filepath+"account_file.txt") as user_info:            #打开用户账号文件
        for account in user_info:                               #查看输入的用户是否再账号文件内
            account_user = account.strip().split(" ")[0]
            account_pass = account.strip().split(" ")[1]
            account_status = account.strip().split(" ")[2]
            account_type = account.strip().split(" ")[3]
            #判断是否已锁定账户
            if account_user==username and account_status=="N":
                dic ={"file":"","token":"","message":"false","resultcode":-3}    #否则密码错误，resultcode=-3 账号被锁定
                    #retufile=re.returnfile(dic)
                return dic
            if username == account_user and typefile==account_type:                        #如果输入的用户名在用户文件中存在
                if password == account_pass:    #密码正确，则判断登录成功
                        power_read = open(filepath+"power_"+typefile+".txt","r")#读取权限
                        #print(power_read)
                        for power in power_read:
                            power_user = power.strip().split(" ")[0]        #取出power文件里面的权限用户名
                            if username == power_user: 
                                power_html=power.strip().split(" ")[1]
                                
                                tokenfile =log.logfile(username,clientaddr)#登录写入记录
                                
                                dic ={"file":power_html,"token":tokenfile,"message":"true","resultcode":1}
                                #retufile=re.returnfile(dic)
                                return dic #returnfile(dic)
                            else:
                                continue              
                else:
                    logk.loglock(username,clientaddr)
                    dic ={"file":"","token":"","message":"false","resultcode":-2}    #否则密码错误，resultcode=-2 重新输入密码，即可用再输入两次
                    #retufile=re.returnfile(dic)
                    return dic            
                    # for count in range(0,2):
                    #     count = count + 1
                    #     password = input("please input your password:")
                    #     if password == account_pass:
                    #         print("welcome to login")          #如果再次输入的密码正确，则跳出
                    #         break
                    #     else:
                    #         print("wrong password")
                    # if count == 2:                              #如果三次输错，则写入lock文件中，采用追加写入的方式
                    #     lock_write = open("lock_file.txt","a+")
                    #     lock_write.write("\n")
                    #     lock_write.write(username)
                    #     lock_write.close()
        if username == account_user and typefile!=account_type:
            dic ={"file":"","token":"","message":"false","resultcode":-1}    #登陆失败resultcode=-1 没有此账户
            #retufile=re.returnfile(dic)
            return dic
        if username!=account_user:                                     #如果账号文件内没有此账号，则提出没有此用户信息
            dic ={"file":"","token":"","message":"false","resultcode":-1}    #登陆失败resultcode=-1 没有此账户
            #retufile=re.returnfile(dic)
            return dic  
