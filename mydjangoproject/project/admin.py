from django.contrib import admin

from .models import Tag, Quotes, Authors

admin.site.register(Tag)
admin.site.register(Quotes)
admin.site.register(Authors)
