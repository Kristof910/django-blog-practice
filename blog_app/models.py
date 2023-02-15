from django.db import models
from django.urls import reverse
import datetime
from django.contrib.auth.models import User


class IndexInfo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse("index-info", args=[str(self.id)])

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey("Blogger", on_delete=models.SET_NULL, null=True)
    date = models.DateField(default=datetime.date.today)
    body = models.TextField()

    def get_absolute_url(self):
        return reverse("blog-post", args=[str(self.id)])

    def __str__(self):
        return self.title


class Comment(models.Model):
    # this is the logged in user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    blog_post = models.ForeignKey("BlogPost", on_delete=models.RESTRICT)

    def get_absolute_url(self):
        return reverse("comment", args=[str(self.id)])

    def __str__(self):
        return f"BLOG POST: {self.blog_post}, USER: {self.user}"


class Blogger(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    # this will identify which user is the blogger
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("blogger", args=[str(self.id)])

    def __str__(self):
        return self.name
