from flask import Flask, escape, request

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def index():
    met = request.method

    if request.method == 'POST':
        return f'<h1>Hello {request.form.get("name", "WORLD")} </h1>'

    return f'<h1>Hello all</h1>'


# Можно обрабатывать функцию без декоратора route
# app.add_url_rule("/", view_func=index)


@app.route('/hello/')
@app.route('/hello/<string:name>/')
def hello(name=None):
    if name is None:
        name = 'WORLD'
    return f'<h1>Hello {name}</h1>'


@app.route('/post/<int:post_id>')
def show_post_int(post_id):
    return f'Post id = {post_id}{vars()}'


@app.route('/post/<post_id>')
def str_show_post(post_id):
    return f'Post id = {post_id}'
