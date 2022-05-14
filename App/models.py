from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=225)
    author = models.CharField(max_length=25)
    author_desc = models.TextField(blank=True, default="NULL")
    slug = models.CharField(max_length=225)
    body = models.TextField()
    images = models.ImageField(upload_to = "media/",blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    recommended = models.BooleanField(default=False)
    categories = models.ManyToManyField("Category", related_name='posts')

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class ReplyComment(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey('Comment', on_delete = models.CASCADE)

    def __str__(self):
        return self.name

    