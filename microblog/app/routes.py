from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)