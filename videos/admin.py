from django.contrib import admin
from . import models


class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

    class Meta:
        model = models.Video


admin.site.register(models.Video, VideoAdmin)
