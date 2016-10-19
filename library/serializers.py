from library.models import Article, Author, Year
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(many=True)
    date = serializers.StringRelatedField(read_only=True)
    labels = serializers.StringRelatedField(many=True)
    list_strategies = serializers.StringRelatedField(many=True)

    class Meta:
        model = Article
        fields = ('key', 'title', 'author', 'date', 'abstract', 'pages', 'journal', 'labels', 'list_strategies')


class AuthorSerializer(serializers.HyperlinkedModelSerializer):

    papers_on_this_db = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = "__all__"


    def get_papers_on_this_db(self, obj):
        return obj.article_set.count()


class YearSerializer(serializers.HyperlinkedModelSerializer):

    papers_on_specific_year = serializers.SerializerMethodField()

    class Meta:
        model = Year
        fields = "__all__"


    def get_papers_on_specific_year(self, obj):
        return obj.article_set.count()
