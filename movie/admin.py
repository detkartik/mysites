from django.contrib import admin
from .models import Movie, Rating
# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ['title', 'description', 'price',
    #           'published', 'is_published', 'cover']
    list_display = ['title', 'description', 'price',
                    'released', 'is_released', 'cover']
    list_filter = ['title', 'price', 'released']
    search_fields = ['title']


admin.site.register(Rating)
