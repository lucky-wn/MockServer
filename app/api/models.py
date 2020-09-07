# -*- coding: utf-8 -*-
# @Time : 2020/9/7 7:55
# @Author : ning
# @File : models.py
from datetime import datetime

from app import db


# 用户表
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 昵称
    pwd = db.Column(db.String(100))  # 密码
    email = db.Column(db.String(100), unique=True)  # 邮箱
    phone = db.Column(db.String(11), unique=True)  # 手机号码
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 注册时间


# 商品表
class Goods(db.Model):
    __tablename__ = "goods"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 昵称
    price = db.Column(db.String(100))   # 价格
    stock = db.Column(db.Integer)   # 库存
    discount = db.Column(db.Float)  # 折扣
    addtime = db.Column(db.DateTime, default=datetime.now)  # 上架时间
    downtime = db.Column(db.DateTime)  # 下架时间


if __name__ == '__main__':
    db.create_all()
    #db.drop_all()
