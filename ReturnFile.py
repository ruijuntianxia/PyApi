# coding:utf-8
from flask import make_response
import json

def returnfile(file):
    resp = make_response(json.dumps(file))
                            
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    resp.headers['Content-Type']= 'application/json'
          
    return resp