
from functools import wraps
from flask import jsonify, make_response, abort
from flask_jwt_extended import (jwt_required,
                                verify_jwt_in_request, get_jwt_identity)


def admin_allowed(function):
    """allows admin t access"""
    @wraps(function)
    @jwt_required
    def wrapper(*args, **kwargs):
        """wrapper for the function"""
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


def attendant_allowed(function):
    """
    allows access for attendants only
    """
    @wraps(function)
    @jwt_required
    def wrapper(*args, **kwargs):
        """wrapper for the function"""
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


def both_roles_allowed(function):
    """ this allows both the attendant and admin to have access"""
    @wraps(function)
    @jwt_required
    def wrapper(*args, **kwargs):
        """wrapper for the function"""
        return function(*args, **kwargs)
    return wrapper
