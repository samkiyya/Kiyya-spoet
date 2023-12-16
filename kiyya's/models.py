from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Poet(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/%y')
    description = models.TextField()

    def __str__(self):
        return self.title


class Quote(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/%y')
    description = models.TextField()


    def __str__(self):
        return self.title
    

class Video(models.Model):
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to='video/%y')
    description = models.TextField()


    def __str__(self):
        return self.title

    
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title