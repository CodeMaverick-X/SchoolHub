#!/usr/bin/python3
"""this module is to handle the routes for login"""

from flask import Flask, session, render_template,\
                  request, redirect, g, url_for, jsonify, make_response
import models
from models.user import User
import os
from flask_bcrypt import Bcrypt
from web_dynamic.pages import page_views

bcrypt = Bcrypt()

@page_views.route('/', methods=['GET', 'POST'])
def index():
    """this route directs you to the login page"""
    if request.method == 'POST':
        session.pop('user', None)

        password = request.form['password']
        username = request.form['username']

        if (known_user := models.storage.get_user(username)) and\
           (bcrypt.check_password_hash(known_user.password, password)):
            session['user'] = username
            session['user_id'] = known_user.id
            session['year'] = known_user.current_year
            session['semester'] = known_user.current_semester

            return make_response(jsonify({'success': True}), 200)
        else:
            return make_response(jsonify({'success': False}), 400)
    return render_template('login.html')


@page_views.route('/register', methods=['GET', 'POST'])
def register():
    """this route directs you to the login page"""
    if request.method == 'POST':
        session.pop('user', None)

        password = request.form['password']
        pass_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        username = request.form['username']
        user_info = {'username': username, 'password': pass_hash,
                     'current_year': 1, 'current_semester': 1}

        if models.storage.unique(username):
            user = User(**user_info)
            user.save()
            user.create_events()
        # create user

            session['user'] = username
            session['user_id'] = user.id
            session['year'] = user.current_year
            session['semester'] = user.current_semester
            return jsonify({'success': True,
                            'message': 'Registration successful'})
        else:
            return jsonify({'success': False, 'message': 'username taken'})
    return render_template('login.html')


@page_views.route('/logout', methods=['GET'])
def logout():
    """logout user from session and redirect to home page"""
    session.pop('user', None)

    return redirect(url_for('page_views.index'))


@page_views.route('/home', methods=['GET'])
def home():
    """this route is for the home page"""
    if g.user:
        return render_template('index.html', user=session['user'])
    return redirect(url_for('page_views.index'))


@page_views.route('/settings', methods=['GET'])
def settings():
    """route for settings page"""
    if g.user:
        return render_template('settings.html', user=session['user'])
    return redirect(url_for('page_views.index'))


@page_views.route('/grades', methods=['GET'])
def grades():
    """route for grades page"""
    if g.user:
        return render_template('grades.html', user=session['user'])
    return redirect(url_for('page_views.index'))


@page_views.route('/events', methods=['GET'])
def events():
    """route for events page"""
    if g.user:
        return render_template('events.html', user=session['user'])
    return redirect(url_for('page_views.index'))


@page_views.before_request
def before_request():
    g.user = None

    if 'user' in session:
        g.user = session['user']
