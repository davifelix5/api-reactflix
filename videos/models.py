from django.db import models
from categories.models import Category


class Video(models.Model):
    title = models.CharField(max_length=500, null=False, blank=True)
    url = models.URLField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    youtube_image = models.URLField(null=False, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='videos')
    
    def __str__(self):
        return self.title
