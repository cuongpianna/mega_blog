from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app import app
from app.forms import LoginForm
from app.models import User


@app.route('/')
@login_required
def hello_world():
    user = {'username': 'Cuong'}
    return render_template('index.html', title='Home', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('/'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        print(user.password_hash)
        if user is None:
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('/'))
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for(''))
