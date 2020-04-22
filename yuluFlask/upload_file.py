# -*- coding:utf-8 -*-
# @Time   ：2020/4/21 21:47
# @Author ：mingfei_liao
# @File   ：upload_file.py
from flask import request,Flask,render_template
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

#upload_path = 'D:\projectCode\learn_python3\yuluFlask\'   # 上传路径
types = set(['png', 'bmp',  'jpg', 'jpeg'])   # 允许上传的文件类型
#app.config['upload_path'] = upload_path

@app.route('/')
def index():
    return render_template('hello.html')

def allowed_file(filename):   # 验证上传的文件名是否符合要求，文件名必须带点并且符合允许上传的文件类型要求，两者都满足则返回 true
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in types

@app.route('/upload', methods=['GET', 'POST'])
def upload_file_test():
    if request.method == 'POST':
        f = request.files.get['fileupload'] #获取上传的文件
        if f and allowed_file(f.filename): # 如果文件存在并且符合要求则为 true
            filename = secure_filename(f.filename)  # 获取上传文件的文件名
            f.save(os.path.abspath(os.path.dirname(__file__)) ,filename)  # 保存文件
            return '{} upload successed!'.format(filename)  # 返回保存成功的信息


