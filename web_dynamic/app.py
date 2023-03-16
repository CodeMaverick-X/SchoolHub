#!/usr/bin/python3
"""this module is to handle the routes for login"""

from flask import Flask, session, render_template, request, redirect, g, url_for

import os

app = Flask(__name__)

app.secret_key = 'my_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session.pop('user', None)

        if request.form['password'] == 'password':
            session['user'] = request.form['username']
            return redirect(url_for('protected'))
    return render_template('login.html')

@app.route('/protected')
def proetcted():
    if g.user:
        return render_template('home.html', user=session['user'])
    return redirect(url_for('login.html'))

@app.before_request
def before_request():
    g.user = None

    if 'user' in session:
        g.user = session['user']


if __name__ == "__main__":
    app.run(debug=True, port="5000")
