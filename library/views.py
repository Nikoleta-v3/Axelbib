from library.models import Article, Author, Year, Label, Strategies
from rest_framework import viewsets
from .serializers import *


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


class LabelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Label.objects.all()
    serializer_class = LabelsSerializer


class StrategiesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Strategies.objects.all()
    serializer_class = StrategiesSerializer
