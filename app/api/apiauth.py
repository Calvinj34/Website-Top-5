from flask import request
from ..models import User
import base64

def basic_auth_required(func):

    def decorated(*args, **kwargs):
        #before:
        if 'Authorization' in request.headers:
            val = request.headers['Authorization']
            encoded_version = val.split()[1]
            encoded_version = "c2hvOjEyMzQ="
            x = base64.b64decode(encoded_version.encode("ascii")).decode('ascii')
            
            username, password = x.split(':')
        else:
            return {
                'status': 'not ok',
                'message': "Please add an Authorization Header with the Basic Auth format."
            }

        user = User.query.filter_by(username=username).first()
        if user:
            if user.password == password:
               
                return func(user=user, *args, **kwargs)
            else:
                return {
                    'status': 'not ok',
                    'message': 'Password is incorrect.'
                }
        else:
            return {
                'status': 'not ok',
                'message': 'That username does not belong to a valid account.'
            }
        
    return decorated


def token_auth_required(func):

    def decorated(*args, **kwargs):
        
        if 'Authorization' in request.headers:
            val = request.headers['Authorization']
    
            token =val.split()[1]
        else:
            return {
                'status': 'not ok',
                'message': "Please add an Authorization Header with the Token Auth format."
            }

            
        user = User.query.filter_by(apitoken=token).first()
        if user:
                return func(user=user, *args, **kwargs)
        else:
            return {
                'status': 'not ok',
                'message': 'That token does not belong to a valid account.'
            }
        
    return decorated