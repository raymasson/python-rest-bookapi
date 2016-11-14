from mongoengine import *

class Book(Document):
    title = StringField()
    author = StringField()
    genre = StringField()
    read = BooleanField(default=False)