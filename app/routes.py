from app import app
from flask import url_for, render_template,send_from_directory
import os

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about_me')
def about_me():
    return render_template('about_me.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'static/images/favicon.png', mimetype='image/vnd.microsoft.icon')