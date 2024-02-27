from django import template

register = template.Library()
def tags(quote):
    return ", ".join([str(name) for name in quote.all()])

register.filter("tags", tags)