import logging
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.config['ENV'] = 'development'
# 设置session的key
app.config['SECRET_KEY'] = 'hdf6735hjdfh8'


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 验证用户名是否为admin
        username = request.form.get('username')
        if username == 'admin':
            # 不通过模板渲染,闪现传递消息
            flash('恭喜！验证成功啦', 'info')
            flash('哈哈哈', 'error')
            flash(username, 'warning')
            return redirect(url_for('index'))
        else:
            # 使用app自带logger 输出到terminal中
            app.logger.debug('这是一个debug测试') # 为app时，输出到terminal中 为flask.app，WARNING输出到文件中
            app.logger.error('这个是一个error测试')
            app.logger.warning('这个是一个warning测试')
    return render_template('login.html',msg = '请登录') # 原先传递值的方式


# 日志配置 python的logging模块
# logger = logging.getLogger('flask.app') # 为flask.app时 app.logger.* 所有都输出到terminal中
logger = logging.getLogger('app') # app时 app.logger.* 级别高于WARNING时输出到文件中
logger.setLevel(level=logging.WARNING) # 级别高于时输出
handler = logging.FileHandler("log/log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

@app.route('/index')
def index():
    # python的logging模块将其写入文件
    logger.warning('logging对首页的警告！！！！')
    # app自带logger 输出到terminal中
    app.logger.warning('app自带logger对首页的警告。。。。')
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)