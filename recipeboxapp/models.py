from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=80)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE())

    def __str__(self):
        return self.name

class Profile(models.Model):
    pass


class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    time_required = models.CharField(max_length=20)
    instructions = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} - {self.author.name}"
# Create your models here.
