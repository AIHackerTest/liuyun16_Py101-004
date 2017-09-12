from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/", methods=['GET','POST'])#为什么调用模板也需要用一下这个app.装饰器？还要用到方法？
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods = ['GET'])#为什么调用模板也需要用一下这个app.装饰器？
def signin_form():
    return """<form action="/signin" method="post">
                <p><input name="username"></p>
                <p><input name="password" type="password"></p>
                <p><button type="submit">Sign In</button></p>
                </form>""" #获取用户输入，如何存储到request对象的？运用了<form><input><button>等元素

@app.route("/signin", methods=['POST'])#为什么调用模板也需要用一下这个app.装饰器？
def signin():
    #需要从request对象读取表单内容：
    if request.form['username'] == 'admin' and request.form['password'] == 'password':#如何调用form方法的？
        return '<h3>Hello, admin!</h3>'
    else:
        return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()
