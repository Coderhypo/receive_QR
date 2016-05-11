#!/usr/bin/env python
# coding=utf-8
from flask import request, redirect

from app import app


@app.route('/')
def gateway():
    agent = request.headers.get('User-Agent')
    agent = agent.lower()

    if agent.find('micromessenger') != -1:
        return "wechat"

    if agent.find('alipay') != -1:
        return "alipay"

    return 'please use wechat or alipay'
