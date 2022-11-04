import os

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from flask import Flask, request
from flask_swagger_ui import get_swaggerui_blueprint


print ('__init__ app')
app = Flask(__name__)
"""
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ \
                os.path.join(basedir, 'db.sqlite3')

"""
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///adb.sqlite3'
app.config['SECRET_KEY'] = "random string"


db = SQLAlchemy(app)
ma = Marshmallow(app)


from app.course_api import course_api
app.register_blueprint(course_api,url_prefix='')


### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "rapp"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)



with app.app_context():
    print ('db creation ..')
    db.create_all()

app.run()