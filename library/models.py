from django.db import models

class Article(models.Model):
   title = models.TextField()
   author = models.TextField()
   date = models.DateTimeField()
   abstract = models.TextField()
   key = models.TextField(blank=True, unique=True)


   def __str__(self):
      return "{} - {}".format(self.key, self.title)