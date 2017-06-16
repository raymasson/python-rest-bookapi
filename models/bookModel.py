from mongoengine import *

class Books(Document):
    title = StringField()
    author = StringField()
    genre = StringField()
    read = BooleanField(default=False)