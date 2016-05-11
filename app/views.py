#!/usr/bin/env python
# coding=utf-8
from flask import request, redirect

from app import app
from config import ALIPAY_URL, TENPAY_URL


@app.route('/')
def gateway():
    agent = request.headers.get('User-Agent')
    agent = agent.lower()

    if agent.find('micromessenger') != -1:
        return redirect(TENPAY_URL)

    if agent.find('alipay') != -1:
        return redirect(ALIPAY_URL)

    return 'error'
