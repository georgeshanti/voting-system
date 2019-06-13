import yaml
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder="build/static", template_folder="build")

config = {}

with open('/home/george/Others/voting/voting-system/config.yaml') as config_file:
    config = yaml.safe_load(config_file)
    db_config = config['db_server']

url = ('{0}://{1}:{2}@{3}/{4}').format(db_config['server'], db_config['user'], db_config['password'], db_config['host'], db_config['db_name'])
app.config['SQLALCHEMY_DATABASE_URI'] = url
db = SQLAlchemy(app)