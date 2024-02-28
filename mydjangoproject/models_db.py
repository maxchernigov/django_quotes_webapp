from mongoengine import EmbeddedDocument, Document, CASCADE
from mongoengine.fields import BooleanField, DateTimeField, EmbeddedDocumentField, ListField, StringField, ReferenceField


class Authors(Document):
    fullname = StringField(required=True)
    born_date = StringField(required=True)
    born_location = StringField(required=True)
    description = StringField(required=True)


class Qoutes(Document):
    tags = ListField(StringField())
    author = ReferenceField(Authors, reverse_delete_rule=CASCADE)
    quote = StringField()