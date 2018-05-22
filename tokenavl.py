# coding:utf-8
import os
import ReturnFile as re


def posttoke(filed):
    tokenfile=filed['token']
    username= filed['name']
    filepath=os.getcwd()+"\\config\\"
    login_read = open(filepath+"login_file.txt","r")#读取权限
    
    loginlog=0
    nusum=0
    for login in login_read:
        if nusum==0:
            nusum+=1
            continue
        else:
            login_user = login.strip().split(",")[0]      #取出power文件里面的权限用户名       
            login_token = login.strip().split(",")[3] # 取出用户名对用token
            if username == login_user: 
                loginlog=1
                if tokenfile==login_token:
                    loginlog=2
                    break
    if loginlog==2:
        dic ={"file":"","message":"true","resultcode":1}    #否则密码错误，resultcode=-2 重新输入密码，即可用再输入两次
        #retufile=re.returnfile(dic)
        return dic 
       
    else:
        dic ={"file":"","message":"false","resultcode":-1}    #否则密码错误，resultcode=-2 重新输入密码，即可用再输入两次
        #retufile=re.returnfile(dic)
        return dic 
            
   
