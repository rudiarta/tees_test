from functools import wraps
from flask import request, Response

def UserMiddleware(func):
    @wraps(func)
    def decoreted_func(*args, **kwargs):
        # return Response("Failed", mimetype='text/plain', status=401)
        # print(request.headers['token'])
        return func(*args, **kwargs)
    return decoreted_func
