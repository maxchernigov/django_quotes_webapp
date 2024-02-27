from mongoengine import Document, StringField, ListField, ReferenceField
from connect_to_mongo import connect


class Authors(Document):
    fullname = StringField(required=True)
    born_date = StringField(required=True)
    born_location = StringField(required=True)
    description = StringField(required=True)


class Quotes(Document):
    tags = ListField(StringField(), required=True)
    author = ReferenceField(Authors, required=True)
    quote = StringField(required=True)