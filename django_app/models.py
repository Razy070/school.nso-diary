from django.db import models


# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=200)
    rating = models.IntegerField(blank=True, null=True, default=False)
    published = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
