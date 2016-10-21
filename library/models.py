from django.db import models
from django.core.validators import MaxValueValidator


class Author(models.Model):
    """A class for the authors"""
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Year(models.Model):
    """A class for the Years"""
    year = models.PositiveIntegerField(unique=True, validators=[MaxValueValidator(9999)])

    def __str__(self):
        return "{}".format(self.year)


class Label(models.Model):
    """A class for the labels"""
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label


class Strategies(models.Model):
    """A class for the list of strategies"""
    strategy_name = models.CharField(max_length=300, unique=True)
    description = models.TextField(blank=True)
    implemented = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.strategy_name


class Article(models.Model):
    """A class for the article

      Parameters:

      - title: Title (TextField)
      - author: Name of Author (CharField)
      - date: Published Year (IntegerField)
      - abstract: Abstract (TextField)
      - key: A unique citation (CharField)
      - labels: Labels for both the tournament type and the strategies (CharField)
      - pages: Number of pages (IntegerField)
      - journal: Journal (TextField)
      - ISBN: ISBN (CharField)
      """
    title = models.TextField(blank=True)
    author = models.ManyToManyField(Author)
    date = models.ForeignKey(Year)
    abstract = models.TextField(blank=True)
    key = models.CharField(unique=True, max_length=20)
    labels = models.ManyToManyField(Label)
    pages = models.CharField(max_length=10, blank=True)
    journal = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    list_strategies = models.ManyToManyField(Strategies, blank=True)
    read = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return "{} - {}".format(self.key, self.title)

