from django.db import models

class Article(models.models):
   title = models.TextField()
   author = models.TextField()
   date = models.DateTimeField()
   abstract = models.TextField()
   
