from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Post(models.Model):
    header = models.CharField(max_length = 300)
    discription = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add = True)
    datePublic = models.DateTimeField(blank = True)
    categorys = models.ManyToManyField(Category)

    def __str__(self):
        return self.header

    def save(self, *args, **kwargs):
        self.datePublic = timezone.now()
        return super(Post, self).save(*args, **kwargs)