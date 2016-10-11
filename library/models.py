from django.db import models


class Author(models.Model):
    """A class for the authors"""
    author = models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(self.author)


class Year(models.Model):
    """A class for the Years"""
    year = models.IntegerField()

    def __str__(self):
        return "{}".format(self.year)


class Label(models.Model):
    """A class for the labels"""
    label = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.label)


# class Strategies(models.Model):
#    """A class for the strategies"""


class Article(models.Model):
    """A class for the article

      Parameters:

      - title: Title (TextField)
      - author: Name of Author (CharField)
      - date: Published Year (IntegerField)
      - abstract: Abstract (TextField)
      - key: A unique citation (CharField)
      - labels: Labels for both the tournament type and the strategies (CharField)
      - num_pages: Number of pages (IntegerField)
      - journal: Journal (TextField)
      - isbn: ISBN (CharField)
      """
    title = models.TextField(blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default="Empty")
    date = models.ForeignKey(Year, on_delete=models.CASCADE, default="Empty")
    abstract = models.TextField()
    key = models.CharField(blank=True, unique=True, max_length=10)
    labels = models.ForeignKey(Label, on_delete=models.CASCADE, default="Empty")
    num_pages = models.CharField(max_length=4, blank=True)
    journal = models.TextField(blank=True)
    isbn = models.CharField(unique=True, max_length=13, blank=True)

    def __str__(self):
       return "{} - {}".format(self.key, self.title)
