from app import mongo

class User(mongo.Document):
    username = mongo.StringField(required=True, unique=True)
    password = mongo.StringField(required=True)
    is_admin = mongo.BooleanField(default=False)

class DataTable(mongo.Document):
    name = mongo.StringField(required=True)
    schema = mongo.StringField(required=True)
    database = mongo.StringField(required=True)