from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Jansen'}
    posts = [
        {
            'author': 'Jansen',
            'body': 'Gosto muito de violão!'
        },
        {
            'author': 'Daniele',
            'body': 'Sou muito simpática!'
        },
        {
            'author': 'Lucas',
            'body': 'Os melhores filmes são os da UCM!'
        },
        {
            'author': 'Lorenzo',
            'body': 'Adora andar de bicileta!'
        },
        {
            'author': 'Lorena',
            'body': 'Quero muito ir para a TEEN fest!'
        },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)