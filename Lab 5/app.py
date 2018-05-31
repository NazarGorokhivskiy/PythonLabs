from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import sys
from views import *

app = Flask(__name__)
ma = Marshmallow(app)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)


sys.path.insert(0, 'views')

if __name__ == '__main__':
    app.run()
