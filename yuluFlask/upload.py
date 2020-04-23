from flask import Flask,request,render_template,jsonify
from werkzeug.utils import secure_filename
import os
import time
import random

app=Flask(__name__)
app.config['JSON_AS_ASCII'] = False

file_types = set(['png','jpg','jpge','bmp'])
file_path='/Users/panmeicha/code/upload'

def file_type(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in file_types

def file_name():
    current_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    random_number = random.randint(100, 999)
    filename = str(current_time) + str(random_number)
    return filename

@app.route('/',methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['photo']
        if file_type(f.filename):
            fname=secure_filename(f.filename)
            type = fname.rsplit('.', 1)[1]
            new_filename = file_name() + '.' + type
            f.save(os.path.join(file_path, new_filename))
            return '<h1>上传成功</h1>'
        else:
            return jsonify({"success": 99999, "msg": "上传失败"})
    return render_template('upload.html')

if __name__=='__main__':
    app.run()