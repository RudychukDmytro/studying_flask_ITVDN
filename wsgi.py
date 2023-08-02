from flask import Flask, render_template

app = Flask(__name__)

def get_films():
    return [
        {
            'id': 1,
            'title': 'Harry Potter and the Philosoper`s Stone',
            'release_date': 'November 4, 2001'
        },
        {
            'id': 2,
            'title': 'Harry Potter and the Chamber of Secrets',
            'release_date': 'November 3, 2002'
        },
        {
            'id': 3,
            'title': 'Harry Potter and the Prisoner of Azkaban',
            'release_date': 'May 31, 2004'
        },
        {
            'id': 4,
            'title': 'Harry Potter and the Goblet of Fire',
            'release_date': 'November 18, 2005'
        }
    ]


@app.route("/")
@app.route("/hello")
def index():
    films = get_films()
    return render_template("hello.html", films=films)

@app.route("/about")
def about():
    return render_template("about.html", title='About')

@app.route("/name/<string:name>")
def name(name: str):
    return f'<h1>Hello, {name.capitalize()}</h1>'

if __name__ == "__main__":
    app.run()