from flask import Flask, request

from views import product_app

app = Flask(__name__)
app.register_blueprint(product_app, url_prefix="/products")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return f"<h1>Hello {request.form.get('name', 'World')}!</h1>"
    return "<h1>Hello world!</h1>"


