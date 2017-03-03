from django.db import models
from django.utils import timezone


class Article(models.Model):
    """Article moel for the article app."""

    title = models.CharField(max_length=255)
    short_desc = models.CharField(max_length=255, default='', blank=True, null=True)
    long_desc = models.CharField(max_length=1000, default='', blank=True, null=True)
    link = models.CharField(max_length=255)
    votes = models.IntegerField(default=1)
    date_submitted = models.DateTimeField(default=timezone.now)
