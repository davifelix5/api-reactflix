from django.contrib import admin
from . import models


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'priority']

    class Meta:
        model = models.Category


admin.site.register(models.Category, CategoryAdmin)
