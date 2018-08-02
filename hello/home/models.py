from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    post=models.TextField()
    user=models.ForeignKey(User)
    date=models.DateTimeField(auto_now=True)
    title=models.CharField(max_length=100,default='')

    def __str__(self):
        return self.post


class Comment(models.Model):
    post = models.ForeignKey('home.Post', on_delete=models.CASCADE, related_name='comments',null=True)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
