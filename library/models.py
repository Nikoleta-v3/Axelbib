from django.db import models
from django.core.validators import MaxValueValidator


class Author(models.Model):
    """
    A module for representing an author

    Attributes:
    ----------
    - name: Character Field
    """
    name = models.CharField(max_length=200, )

    def __str__(self):
        return self.name


class Year(models.Model):
    """
    A module for representing the year of publication

    Attributes:
    ----------
    - year: Positive Integer Field

    """
    year = models.PositiveIntegerField(validators=[MaxValueValidator(9999)], unique=True)

    class Meta:
        ordering = ['year']

    def __str__(self):
        return "{}".format(self.year)


class Label(models.Model):
    """
    A module for representing labels of the article.

    Labels are used mainly by me to categorize the papers
    I have read. For example, Simple, Noisy, Spatial tournaments.

    Attributes:
    ----------
    - label: Char Field
    """
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label


class Strategies(models.Model):
    """
    A module for representing the strategies used by the
    author for his/her article research.

    Attributes:
    ----------
    - strategy_name: Char Field
            the name of a strategy
    - description: Text Field
            a simple description of the strategy
    - implemented : Char Field
            whether the strategy has been implemented in Axelrod python library or not
            (this could possible change in the future and become Choice Field)
    """
    strategy_name = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    implemented = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.strategy_name


class Article(models.Model):
    """
    A module for representing an article

    Attributes:
    -----------

    - title: Text Field
        the title of the article
    - author: Many to Many Field
        a list of authors of the article
    - date: Foreign Key Field
        the year of publication
    - abstract: Text Field
        the abstract of the article
     - key: Char Field
        a unique key for citation. Looks similar to the Mendeley key
    - labels: Many to Many Field
        labels for the article
    - pages: Integer Field
        the pages the article is within the journal
    - journal: Text Field
        the journal the article was published
    - notes: Text Field
        personal notes for each article when I read it
    - list_strategies: Many to Many Field
        a list of strategies
    - read: Boolean Field
        true when I have read file, false otherwise
    """
    title = models.TextField(blank=True)
    author = models.ManyToManyField(Author)
    date = models.ForeignKey(Year)
    abstract = models.TextField(blank=True)
    key = models.CharField(unique=True, max_length=20)
    labels = models.ManyToManyField(Label, blank=True)
    pages = models.CharField(max_length=10, blank=True)
    journal = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    list_strategies = models.ManyToManyField(Strategies, blank=True)
    read = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return "{} - {}".format(self.key, self.title)

