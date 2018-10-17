import os
from app import create_app

# get current config from enviroment variable
config_name = os.getenv('APP_SETTINGS')

# create app from the config
app = create_app(config_name)

# run the app
if __name__ == '__main__':
    app.run()
