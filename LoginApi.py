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
import LoginAvl as loga
import tokenavl as to
import os



app = Flask(__name__)

CORS(app, resources=r'/*')
@app.route('/login/', methods=['GET', 'POST'])
# 定义函数，参数是函数的两个参数，都是python本身定义的，默认就行了。
def application():
    #post数据
    filed=request.data
    #IP
    Clientaddr=request.remote_addr

    #转码，将字节转换为字串
    filed=filed.decode()
    #处理转换为json
    filed=json.loads(filed) 
    #登录验证
    dic=loga.postLogin(filed,Clientaddr) 
    #返回值
    retufile=re.returnfile(dic)
    return retufile  


@app.route('/logintk/', methods=['GET', 'POST'])
# 定义函数，参数是函数的两个参数，都是python本身定义的，默认就行了。
def apptokenfile():
    filed=request.data
    #fileurl=request.environ
    #print(fileurl)
    filed=filed.decode()
    filed=json.loads(filed) 
    dic=to.posttoke(filed)
    retufile=re.returnfile(dic)
    return retufile 

    


if __name__ == "__main__":
    

    app.run(host="0.0.0.0",port=8009,debug=True)
    #app.run(host="localhost",port=8009)
    #app.run(host="172.18.218.223",port=8009)