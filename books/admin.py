# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Book, BookNumber, Character, Author

# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # fields = ['title', 'description', 'price',
    #           'published', 'is_published', 'cover']
    list_display = ['title', 'description', 'price',
                    'published', 'is_published', 'cover']
    list_filter = ['title', 'price', 'published']
    search_fields = ['title']


admin.site.register(BookNumber)
admin.site.register(Character)
admin.site.register(Author)
