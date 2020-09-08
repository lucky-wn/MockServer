# -*- coding: utf-8 -*-
# @Time : 2020/9/7 7:55
# @Author : ning
# @File : views.py
import uuid

from flask import request, jsonify, session

from . import api


@api.route("/regist/", methods=["POST"])
def regist():
    data = request.form
    username = data.get("username")
    password = data.get("password")
    # 用户名或密码不可以为空
    if not all([username, password]):
        msg = "用户名或密码为空"
        code = "10001"
    if len(username) > 10 or len(username) < 5:
        msg = "用户名长度在5-10之间"
        code = "10002"
    if len(password) > 10 or len(password) < 5:
        msg = "密码长度在5-10之间"
        code = "10003"
    session[username] = password
    msg = "注册成功"
    code = "10000"
    return jsonify({"msg": msg, "code": code})


@api.route("/login/", methods=["POST"])
def login():
    data = request.form
    username = data.get("username")
    password = data.get("password")
    if not all([username, password]):
        msg = "用户名或密码为空"
        code = "20001"
        session_id = ""
    user = session.get(username)
    if not user:
        msg = "用户不存在"
        code = "20002"
        session_id = ""
    if user != password:
        msg = "密码不正确"
        code = "20003"
        session_id = ""
    msg = "登录成功"
    code = "20000"
    session_id = uuid.uuid4().hex
    return jsonify({"msg": msg, "code": code, "sessionId": session_id})


@api.route("/goods/", methods=["GET"])
def goods():
    good = {
        "1":{
            "name":"卷笔刀",
            "price": 22
        },
        "2":    {
            "name": "水杯",
            "price": 55
        }
    }
    return jsonify(good)


@api.route("/buy/", methods=["POST"])
def buy():
    data = request.form
    session_id = data.get("sessionId")
    if not session_id:
        return jsonify({"msg": "用户未登录", "code": "40001"})
    return jsonify({"msg": "购买成功", "code": "400002"})
