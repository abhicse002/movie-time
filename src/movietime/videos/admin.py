from django.contrib import admin

# Register your models here.
from django.utils.html import format_html

from .models import Videos,VideoProxy,VideoProxyforEdu


@admin.register(Videos)
class VideoAdmin(admin.ModelAdmin):
    pass;

@admin.register(VideoProxy)
class VideoProxyAdmin(admin.ModelAdmin):
    list_display = ('videos_id','title' , 'description','pk','length_in_min')
    list_filter = ['title']
    search_fields = ['title']

    class Meta:
        model = VideoProxy

    def get_queryset(self, request):
        return VideoProxy.objects.filter(length_in_min=120)

@admin.register(VideoProxyforEdu)
class VideoProxyAdminforEdu(admin.ModelAdmin):
    list_display = ('videos_id','title' , 'description','pk','length_in_min')
    list_filter = ['title']
    search_fields = ['title']

    class Meta:
        model = VideoProxyforEdu

    def get_queryset(self, request):
        res =  VideoProxy.objects.filter(title="edu videos")
        return res






