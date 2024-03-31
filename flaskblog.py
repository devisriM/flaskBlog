from flask import Flask, render_template, url_for

app = Flask(__name__)


posts = [
    {
        'author': 'Devi',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'May 20, 2023'
    },
    {
        'author': 'Sri',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2022'
    }
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts, title='Home')

@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
