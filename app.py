# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 10:50:34 2019

@author: Korino
"""

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
import datetime
from resources.store import Store, StoreList


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='jose'
api=Api(app)



#app.config['JWT_AUTH_URL_RULE'] = '/login'                              #kreira /login umjesto /auth potrebno promijenit endpoint u Postmanu
jwt=JWT(app,authenticate,identity)                                       #JWT kreira /auth endpoint

app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(seconds=1800)    #JWT istice tek nakon pola sata
#app.config['JWT_AUTH_USERNAME_KEY'] = 'email'                           #auth key postaje email umjesto username

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')

if __name__=='__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)











