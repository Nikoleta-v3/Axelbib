from django.db import models

class Article(models.Model):
   title = models.TextField()
   author = models.TextField()
   date = models.DateTimeField()
   abstract = models.TextField()

