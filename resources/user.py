# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 13:45:43 2019

@author: Korino
"""
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='This field can´t be left blank')
    parser.add_argument('password', type=str, required=True, help='This field can´t be left blank')
    
    def post(self):
        data=UserRegister.parser.parse_args()
        
        if UserModel.find_by_username(data['username']):     #is not None
            return {'message':'User with that name already exists'},400
        
        user=UserModel(**data)  #Umjesto data['username'],data['price'] zato jer i objekt ima isti raspored argumenata
        user.save_to_db()                          
        
        return {'Message':'User created successfully'},201
    
        