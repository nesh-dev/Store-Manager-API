import os
from app import create_app
from flask import redirect, jsonify


# get current config from enviroment variable
config_name = os.getenv('APP_SETTINGS')

# create app from the config
app = create_app(config_name)


@app.route('/docs')
def docs():
    return redirect('https://storemanagerv2.docs.apiary.io')


@app.route('/')
def home():
    return jsonify({"mesage": "welcome to Store Manager API"})

# run the app
if __name__ == '__main__':
    app.run()

