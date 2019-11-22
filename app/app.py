from flask import Flask, redirect, url_for, request, render_template, abort, flash, jsonify

app = Flask(__name__,)


app.secret_key = 'random string'
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None


    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
            request.form['password'] != '123456':
            error = '密码错误，重新输入'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))


    return render_template('login.html', error = error)

@app.route('/api/choose', methods = ['GET', 'POST'])
def choose():
    return '[{"id":"1","date":"2016-10-18","name":"章邯","address":"上海市普陀区"},{"id":"2","date":"2017-05-04","name":"李四","address":"上海市杨浦区"},{"id":"3","date":"2017-08-16","name":"张三","address":"上海市虹口区"},{"id":"4","date":"2018-05-03","name":"王二小","address":"北京康复路58号"}]'


@app.route('/api/menu/user/menus', methods = ['POST'])
def menus():
    return 'this is meuns'


# 后端接受参数
# @app.route('/api/delete', methods = ['POST'])
# def deleteTable():
#     data =request.form['data']
#     if data == 0:
#         return '{"id":"2","date":"2017-05-04","name":"李四","address":"上海市杨浦区"},{"id":"3","date":"2017-08-16","name":"张三","address":"上海市虹口区"},{"id":"4","date":"2018-05-03","name":"王二小","address":"北京康复路58号"}]'
#     elif data == 1:
#         return '[{"id":"1","date":"2016-10-18","name":"章邯","address":"上海市普陀区"},{"id":"3","date":"2017-08-16","name":"张三","address":"上海市虹口区"},{"id":"4","date":"2018-05-03","name":"王二小","address":"北京康复路58号"}]'
#     elif data == 2:
#         return '[{"id":"1","date":"2016-10-18","name":"章邯","address":"上海市普陀区"},{"id":"2","date":"2017-05-04","name":"李四","address":"上海市杨浦区"},{"id":"4","date":"2018-05-03","name":"王二小","address":"北京康复路58号"}]'
#     elif data == 3:
#         return '[{"id":"1","date":"2016-10-18","name":"章邯","address":"上海市普陀区"},{"id":"2","date":"2017-05-04","name":"李四","address":"上海市杨浦区"},{"id":"3","date":"2017-08-16","name":"张三","address":"上海市虹口区"}]'
#




if __name__ == '__main__':
    app.run(debug=True)
