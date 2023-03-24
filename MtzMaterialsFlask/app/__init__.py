# Flask imports for the web application, allows templates and url based commands to work
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache

app = Flask(__name__)
# Conection String used for mysql
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/mtz-materials'

# Connection String used for a sqlitte database.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Orders.db'
app.config['CACHE_TYPE'] = 'simple'
cache = Cache(app)

# db.init_app(app)
# app.app_context().push()
db = SQLAlchemy(app)
# allows database to be created
app.app_context().push()


from app import routes