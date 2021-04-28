from django.contrib import admin

# Register your models here.
from .models import Videos,VideoProxy

admin.site.register(Videos)
admin.site.register(VideoProxy)