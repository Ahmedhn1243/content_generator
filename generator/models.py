from django.db import models

# Create your models here.

from django.db import models

class Content(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tone = models.CharField(max_length=50)

