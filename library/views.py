from library.models import Article, Author, Year
from rest_framework import viewsets
from .serializers import ArticleSerializer, AuthorSerializer, YearSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class YearViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Year.objects.all().order_by('year')
    serializer_class = YearSerializer