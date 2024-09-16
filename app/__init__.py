from flask import Flask
import os
import yaml
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_mongoengine import MongoEngine

app = Flask(__name__)

# Load configurations
config_path = os.path.join(os.path.dirname(__file__), '../config/config.yaml')
with open(config_path, 'r') as f:
    config = yaml.safe_load(f)

app.config.update(config)

# Setup SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{config['mysql']['user']}:{config['mysql']['password']}@{config['mysql']['host']}:{config['mysql']['port']}/{config['mysql']['database']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Setup MongoEngine
app.config['MONGODB_SETTINGS'] = {
    'host': config['mongodb']['uri'],
    'db': config['mongodb']['database']
}
mongo = MongoEngine(app)

# Setup JWT
jwt = JWTManager(app)

# Import routes
from app.routes import auth, dummydata, request, migration

# Register blueprints
app.register_blueprint(auth.bp)
app.register_blueprint(dummydata.bp)
app.register_blueprint(request.bp)
app.register_blueprint(migration.bp)