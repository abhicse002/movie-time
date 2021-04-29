from django.db import models

# Create your models here.
class Videos(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True,null=True)
    videos_id = models.CharField(max_length=100)
    length_in_min = models.IntegerField(default=120)
    class Meta:
        #allows order by wrt to each column
        ordering = ('videos_id','title' , 'description','pk')

#we can change the way it displays the data in admin site
    def __str__(self):
        return  f'{self.title} , {self.description}'

class VideoProxy(Videos):
    class Meta:
        proxy = True
        verbose_name = "Videos with length 120 minutes"
        verbose_name_plural = "published Videos"

class VideoProxyforEdu(Videos):
    class Meta:
        proxy = True
        verbose_name = "Edu Videos"
        verbose_name_plural = "Educational Video"

