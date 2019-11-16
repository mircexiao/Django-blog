from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class BlogArticles(models.Model):
    title=models.CharField(max_length=300)
    body=models.TextField(max_length=3000)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    publish=models.DateTimeField(default=timezone.now)
    class Meta:
        ordering=('-publish',)
    def __str__(self):
        return self.title