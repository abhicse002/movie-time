from django.db import models

# Create your models here.
class Videos(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True,null=True)
    videos_id = models.CharField(max_length=100)

class VideoProxy(Videos):
    class Meta:
        proxy = True
        verbose_name = "Publisehd v"

