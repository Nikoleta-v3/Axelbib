from django.contrib import admin

from .models import Article, Author, Year, Label, Strategies


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    search_fields = ['title', 'key']
    filter_horizontal = ('author', 'list_strategies', 'labels', )


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
admin.site.register(Year)
admin.site.register(Label)
admin.site.register(Strategies)
