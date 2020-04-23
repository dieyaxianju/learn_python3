from flask import request,Flask,render_template,send_from_directory
import os,datetime,random
from werkzeug.utils import secure_filename

app = Flask(__name__)

upload_path = 'D:\projectCode\learn_python3\yuluFlask'   # 上传路径
types = set(['png', 'bmp',  'jpg', 'jpeg'])   # 允许上传的文件类型
app.config['upload_path'] = upload_path  #app.config 以键值对的形式 保存app的配置信息 D:\projectCode\learn_python3\yuluFlask


@app.route('/')
def index():
    return render_template('hello.html')

def allowed_file(filename):   # 验证上传的文件名是否符合要求，文件名必须带点并且符合允许上传的文件类型要求，两者都满足则返回 true
    return '.' in filename and filename.rsplit('.', 1)[1] in types

@app.route('/upload', methods=['GET', 'POST'])
def upload_file_test():
    if request.method == 'POST':
        f = request.files['fileupload'] #获取上传的文件
        if f and allowed_file(f.filename): # 如果文件存在并且符合要求则为 true
            filename = secure_filename(f.filename)  # 获取上传文件的文件名
            newname = '{0:%Y%m%d%H%M%S%f}'.format(datetime.datetime.now())+''.join([str(random.randint(1,10)) for i in range(5)])
            lastname=newname+'.'+filename.rsplit('.', 1)[1]
            f.save(os.path.join(app.config['upload_path'], lastname)) # 保存文件
            return '{0} 文件上传成功，最终文件名为：{1}'.format(filename,lastname)  # 返回保存成功的信息
        else:
            return '文件格式错误，上传失败 '  # 返回失败信息

if __name__=='__main__':
    app.run()

