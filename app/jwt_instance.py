from flask_jwt_extended import JWTManager

from .api.v1.models.auth import userModel
from .api.v2.models.blacklisted import Blacklisted


jwt = JWTManager()

"""
    Function handles revoked tokens once a user is logged out 
    It checks if token is blacklisted.

"""

@jwt.token_in_blacklist_loader
def check_if_token_is_revoked(decrypted_token):
    jti = decrypted_token['jti']
    status = userModel.check_if_blacklist(jti)
    if status is False:
        status = Blacklisted(jti).check_if_blacklist()
    return status
