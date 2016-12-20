# The examples in this file come from the Flask-SQLAlchemy documentation
# For more information take a look at:
# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#simple-relationships

from datetime import datetime

from rest_api.database import db

#from rest_api.app import bcrypt

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, title, body, category, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.category = category

    def __repr__(self):
        return '<Post %r>' % self.title


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name



class BlogPost(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    author_id = db.Column(db.Integer, ForeignKey('ngo.id'))

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __repr__(self):
        return  "title :{}".format(self.title)


class NGO(db.Model):
    __tablename__ = "ngo"

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    password = db.Column(db.String)
    branches = relationship("NGO_Branch", backref="Parent-Office")
    posts = relationship("BlogPost", backref="author")

    def __init__(self, name,description, password):
        self.name = name
        self.description = description
        self.password = password
        #bcrypt.generate_password_hash(password)

    def __repr__(self):
        return '<name {}'.format(self.name)


class NGO_Branch(db.Model):
    __tablename__= "NGObranch"

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    ngo_id = db.Column(db.Integer, ForeignKey('ngo.id'))
    location_X = db.Column(db.Float, nullable=False)
    location_Y = db.Column(db.Float, nullable=False)
    Requirements = relationship("Requirements", backref="NGObranch")

    def __init__(self,ngo_id,location_X,location_Y):
        self.ngo_id = ngo_id
        self.location_Y = location_Y
        self.location_X = location_X

class Requirements(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    ngo_branch = db.Column(db.Integer, ForeignKey('NGObranch.id'))
    requirementType = db.Column(db.Integer, ForeignKey('RequirementType.id'))
    date_created = db.Column(db.DateTime, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)


    def __init__(self,ngo_branch,quantity, date_created):
        self.ngo_branch = ngo_branch
        self.quantity = quantity
        self.date_created = date_created



class RequirementType(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    type_name = db.Column(db.String, nullable=False)

class Donation(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    requirementType = db.Column(db.Integer, ForeignKey('RequirementType.id'))
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String, nullable=False)

    def __init__(self,requirementType,quantity,status):
        self.requirementType=requirementType
        self.quantity = quantity
        self.status = status




