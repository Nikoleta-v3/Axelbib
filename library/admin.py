from django.contrib import admin
from .models import Article, Author, Year, Label

admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Year)
admin.site.register(Label)