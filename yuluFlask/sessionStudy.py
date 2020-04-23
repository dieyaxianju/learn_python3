from flask import Flask,session
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
#设置session
@app.route('/set_session')
def set_session():
    session['username']='admin'
    return 'session设置成功'

#获取session
@app.route('/get_session')
def get_session():
    name = session['username']
    return name

#获取session
@app.route('/del_session')
def del_session():
    session.pop('username')
    return 'session删除成功'
if __name__=='__main__':
    app.run()