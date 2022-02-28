from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=225)
    author = models.CharField(max_length=25, default='Tijano')
    slug = models.CharField(max_length=225)
    body = models.TextField()
    images = models.ImageField(default="Digital18.png",blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    views = models.IntegerField()
    categories = models.ManyToManyField("Category", related_name='posts')

    def __str__(self):
        return self.title
         
class Comment(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete = models.CASCADE)
    user = models.CharField(max_length=20, default='Mall')

    # def __str__(self):
    #     return self.user
    
class ReplyComment(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey('Comment', on_delete = models.CASCADE)
    user = models.CharField(max_length=20, default='Mall')

