from django.db import models

class Post(models.Model):
    header = models.CharField(max_length = 300)
    discription = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add = True)
    datePublic = models.DateTimeField(auto_now = True, editable = True)
    categorys = models.ManyToManyField(Category)

    def __str__(self):
        return self.header

class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name