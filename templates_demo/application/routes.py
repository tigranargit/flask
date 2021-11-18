from werkzeug.utils import redirect
from application import app
from flask import render_template

users = ['ben', 'harry', 'john', 'jane', 'sarah'],

@app.route('/ben')
def ben():
    return render_template('ben.html', users=users)

@app.route('/harry')
def harry():
    return render_template('harry.html', users=users)