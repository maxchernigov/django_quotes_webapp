from django.forms import ModelForm, CharField, TextInput
from .models import Tag, Quotes, Authors


class TagForm(ModelForm):

    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    
    class Meta:
        model = Tag
        fields = ['name']


class AuthorForm(ModelForm):
    fullname = CharField(min_length=3, max_length=25, required=True, widget=TextInput)

    class Meta:
        model = Authors
        fields = ['fullname', 'born_date', 'born_location', 'description']


class QuoteForm(ModelForm):

    quote = CharField(min_length=5, max_length=50, required=True, widget=TextInput())

    class Meta:
        model = Quotes
        fields = ['quote', 'tags', 'author']