from flask_jwt_extended import JWTManager

from .api.v1.models.auth import UserModel
"""
     Holds the the JWT instance to be used in the app
"""
jwt = JWTManager()

"""
    Function handles revoked tokens once a user is logged out 
    It checks if token is blacklisted.

"""


@jwt.token_in_blacklist_loader
def check_if_token_is_revoked(decrypted_token):
    jti = decrypted_token['jti']
    return UserModel.check_if_blacklist(jti)
