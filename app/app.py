from flask import Flask, redirect, url_for, request, render_template, abort, flash

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


if __name__ == '__main__':
    app.run(debug=True)
