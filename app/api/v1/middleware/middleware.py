
from functools import wraps
from flask import request
from flask import jsonify, make_response, abort
from flask_jwt_extended import (jwt_required,
                                verify_jwt_in_request, get_jwt_identity)


"""
    allows acess only to admin
"""


def admin_allowed(function):
    @wraps(function)
    @jwt_required
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_identity()
        if claims['role'] != 2:
            abort(
                make_response(
                    jsonify({'message': 'unauthorized to perform  function'}),
                    401
                )
            )
        return function(*args, **kwargs)
    return wrapper

"""
    allows access for attendants only
"""


def attendant_allowed(function):
    @wraps(function)
    @jwt_required
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_identity()
        if claims['role'] != 1:
            abort(
                make_response(
                    jsonify({'message': 'unauthorized to perform  function'}),
                    401
                )
            )
        return function(*args, **kwargs)
    return wrapper


""" this allows both the attendant and admin to have access"""


def both_roles_allowed(function):
    @wraps(function)
    @jwt_required
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)
    return wrapper

