from django.contrib import admin

from .models import Article, Author, Year, Label, Strategies


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    search_fields = ['title', 'key']
    filter_horizontal = ('author', 'list_strategies', 'labels', )


class AuthorAdmin(admin.ModelAdmin):
    model = Author
    search_fields = ['name']


class StrategiesAdmin(admin.ModelAdmin):
    model = Strategies
    search_fields = ['strategy_name']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Year)
admin.site.register(Label)
admin.site.register(Strategies, StrategiesAdmin)
