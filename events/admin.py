from django.contrib import admin
from .models import Event
# Register your models here.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'day', 'start_time', 'end_time', 'notes']
    list_filter = ['name', 'day']
    search_fields = ['name', 'day']


# admin.site.register(Event)
