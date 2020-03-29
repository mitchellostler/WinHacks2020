# from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime 

# User = settings.AUTH_USER_MODEL

class UserPost(models.Model):
    author = models.ForeignKey(
        User, 
        default=None,
        null=True,
        on_delete=models.CASCADE
        )
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)
    date = models.DateTimeField(default=datetime.now(), blank=True)
