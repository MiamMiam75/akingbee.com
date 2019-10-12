import datetime

from peewee import CharField, TextField, ForeignKeyField, DateTimeField
from .base import BaseModel
from .users import User
from .swarm import SwarmHealth, Swarm
from .apiary import Apiary
from .hive import Hive
from .action import Action



class CommentType(BaseModel):
    fr = CharField()
    en = CharField()
    date_creation = DateTimeField(default=datetime.datetime.now)
    date_modification = DateTimeField(default=datetime.datetime.now)
    

class Comment(BaseModel):
    date = DateTimeField()
    user = ForeignKeyField(User, backref="comments")
    swarm = ForeignKeyField(Swarm, backref="comments", null=True)
    type = ForeignKeyField(CommentType, backref="comments")
    apiary = ForeignKeyField(Apiary, backref="comments", null=True)
    health = ForeignKeyField(SwarmHealth, backref="comments", null=True)
    action = ForeignKeyField(Action, backref="comments", null=True)
    comment = TextField()
    hive = ForeignKeyField(Hive, backref="comments", null=True)
    date_creation = DateTimeField(default=datetime.datetime.now)
    date_modification = DateTimeField(default=datetime.datetime.now)
