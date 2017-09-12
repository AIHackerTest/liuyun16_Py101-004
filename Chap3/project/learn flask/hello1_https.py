from flask import request, Flask
app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/')
def index():
    return 'Index Page'

@app.route('/projects/')  #末尾有尾随斜线/访问时，无论输入这个斜线或不输入，都是返回下面
def projects():
    return 'The project page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()

def do_the_login():
    return "do_the_login()"

def show_the_login_form():
    return "show_the_login_form()"

@app.route('/user/<username>')
def profile(username):
    return 'User %s' % username


if __name__ == '__main__':
    app.run()
