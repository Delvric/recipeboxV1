from django.db import models
from django.utils import timezone


# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
# Create your models here.
