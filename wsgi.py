from flask import Flask

app = Flask(__name__)




@app.route("/")
@app.route("/hello")
def index():
    return '<h1>Hello, world!</h1>'

@app.route("/about")
def about():
    return '<h1>About</h1>'

@app.route("/name/<string:name>")
def name(name: str):
    return f'<h1>Hello, {name.capitalize()}</h1>'

if __name__ == "__main__":
    app.run()