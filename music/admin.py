from django.contrib import admin
from .models import Songs
# Register your models here.


@admin.register(Songs)
class SongAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist']
    list_filter = ['title', 'artist']
    search_fields = ['title']


# admin.site.register(Songs)
