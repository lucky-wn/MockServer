# -*- coding: utf-8 -*-
# @Time : 2020/9/7 7:49
# @Author : ning
# @File : __init__.py.py

from flask import Blueprint

api = Blueprint("api", __name__)

import app.api.views