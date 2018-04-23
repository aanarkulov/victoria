from django.contrib import admin

from news.models import *


class TypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {"slug": ("title",)}


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'pub_date')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Type, TypeAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Subscriber)
