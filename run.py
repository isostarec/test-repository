# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 14:20:59 2019

@author: Korino
"""

from app import app
drom db import db

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()