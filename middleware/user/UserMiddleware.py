from functools import wraps
from flask import request, make_response
import jwt

def UserMiddleware(func):
    @wraps(func)
    def decoreted_func(*args, **kwargs):
        try:
            jwt.decode(request.headers['token'],"secret")
        except:
            return make_response({"status":"unauthorized"}, 401)
              
        return func(*args, **kwargs)
    return decoreted_func
