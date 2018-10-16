from .dummy import users
from ... import create_app


app = create_app(config_name="testing")
client = app.test_client()


def attendant_login_user():
    # to handle error in tests
    client.post('api/v1/register', json=users[8])
    user = client.post('api/v1/login', json=users[8]) 
    attendant_token = ""
    # attendant_token = user.get_json().get('access_token')
    return attendant_token


def admin_login_user():
    # to handle error in tests
    client.post('api/v1/register', json=users[0])
    user = client.post('api/v1/login', json=users[0]) 
    admin_token = ""
    # admin_token = user.get_json().get('access_token')
    return admin_token

attendant_token = attendant_login_user()
admin_token = admin_login_user()


attendant_headers = {
    'Authorization': 'Bearer {}'.format(attendant_token),
    'Content-Type': 'application/json'
}

admin_headers = {
    'Authorization': 'Bearer {}'.format(admin_token),
    'Content-Type': 'application/json'
}
