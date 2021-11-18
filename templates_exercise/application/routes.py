from application import app 
from flask import render_template

names = ['ben', 'harry', 'bob', 'jay', 'matt', 'bill']

@app.route('/nameswithb')
def nameswithb():
    return render_template('nameswithb.html', names=names)