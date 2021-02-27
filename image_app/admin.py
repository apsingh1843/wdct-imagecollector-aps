from django.contrib import admin
from .models import ImageCollector


@admin.register(ImageCollector)
class ImageCollectorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'title', 'photo', 'description', 'date']
