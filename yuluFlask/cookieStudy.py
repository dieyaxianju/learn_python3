from flask import Flask,request
from flask import make_response
import datetime
app = Flask(__name__)
#设置cookies
@app.route('/set_cookie')
def set_cookie():
    resp = make_response('set_cookie')
    resp.set_cookie('password','123456')
    # 通过max_age控制cookie有效期, 单位:秒
    date = datetime.datetime.today() + datetime.timedelta(days=30)
    resp.set_cookie("password2", "hello123",  expires=date)
    return resp

#获取cookies
@app.route('/get_cookie')
def get_cookie():
    name = request.cookies.get('password')
    return name

#获取cookies
@app.route('/del_cookie')
def del_cookie():
    resp = make_response('delete_cookie')
    resp.delete_cookie('password')
    return resp
