from django.conf import settings
from django.db import models

# User = settings.AUTH_USER_MODEL

class UserPost(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
        default =1, 
        null=True, 
        on_delete=models.CASCADE
        )
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)
