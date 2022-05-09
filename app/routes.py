from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'jhon'},
            'body': 'Belo dia em Portland'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'O fime Avengers foi tão legal!'
        }
    ]
    return render_template('index.html', title = 'Home', user=user, posts=posts)