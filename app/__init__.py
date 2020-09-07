# -*- coding: utf-8 -*-
# @Time : 2020/9/7 7:44
# @Author : ning
# @File : __init__.py.py

import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@127.0.0.1:3306/MockServer"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = "bd000d1b0d24487e8cdcf3ad5a0916f5"
app.debug = True
app.config['Upload_DIR'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/")

db = SQLAlchemy(app)

from app.api import api as api_blueprint

app.register_blueprint(api_blueprint, url_prefix="/api")


@app.errorhandler(404)
def page_not_found(error):
    """404"""
    return render_template('home/404.html'), 404
