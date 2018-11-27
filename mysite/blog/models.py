from django.db import models

# 2018/11/21
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    publish_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.publshed_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
