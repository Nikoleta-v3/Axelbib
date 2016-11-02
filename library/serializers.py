from library.models import Article, Author, Year, Label, Strategies
from rest_framework import serializers


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


class LabelsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Label
        fields = ["label"]


class StrategiesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Strategies
        fields = ["strategy_name"]


class ArticleSerializer(serializers.HyperlinkedModelSerializer):

    author = AuthorSerializer(many=True,)
    date = YearSerializer()
    labels = LabelsSerializer(many=True, )
    list_strategies = StrategiesSerializer(many=True)

    class Meta:
        model = Article
        fields = ('key', 'title', 'author', 'date', 'abstract', 'pages', 'journal', 'labels', 'list_strategies')

    def create(self, validated_data):

        # Create the new article attributes
        author = Author.objects.create(name=validated_data['author'])
        date = Year.objects.create(year=validated_data['date'].get("year"))
        label = Label.objects.create(label=validated_data['labels'])
        strategy = Strategies.objects.create(strategy_name=validated_data['list_strategies'])

        # create the article
        article = Article(date=date, title=validated_data['title'], abstract=validated_data['abstract'],
                          key=validated_data['key'], pages=validated_data['pages'],
                          journal=validated_data['journal'])

        article.save()
        article.author.add(author)
        article.labels.add(label)
        article.list_strategies.add(strategy)

        return article

