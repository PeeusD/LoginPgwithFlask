#<------------------database models---->
from . import db  # Impoting from Website package taken from init__py --->db
from flask_login import UserMixin #helps for user to login into dbase
from sqlalchemy.sql import func



class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now()) #func---curent time dt 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  #primarykey will be herei in params
    #foreign key used for 1 to many realtinship as user can have many notes



class User(db.Model, UserMixin): #inheriting params
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique= True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')  #name of the class in pramas which is declated above






