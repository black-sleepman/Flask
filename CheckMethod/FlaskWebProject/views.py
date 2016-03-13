# coding=utf-8
"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template, request
from FlaskWebProject import app

year = datetime.now().year
METHODS = ['GET', 'POST', 'PUT', 'DELETE']


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    name = "Home Page of {0}".format(request.method)
    return render_template(
        'index.html',
        title=name,
        year=year,
    )


@app.route('/test', methods=METHODS)
def test():
    return render_template(
        'custom.html',
        AccessMethod=request.method,
        year=year,
        header=request.headers,
    )
