from django.utils import timezone
from django.db import models

# Create your models here.

class Post(models.Model):
    title =  models.CharField(max_length=120)
    content = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)
