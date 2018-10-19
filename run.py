import os
from app import create_app
from flask import redirect

# get current config from enviroment variable
config_name = os.getenv('APP_SETTINGS')

# create app from the config
app = create_app(config_name)


@app.route('/')
def home():
    return redirect('https://documenter.getpostman.com/view/2464061/RWguvbZ1')

# run the app
if __name__ == '__main__':
    app.run()

