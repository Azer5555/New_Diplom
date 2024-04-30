import datetime
import os
import re
import sqlalchemy.exc
from flask import Flask, make_response
from flask import render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///map.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIрONS'] = False
db = SQLAlchemy(app)


@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html', title='Home')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.2')
