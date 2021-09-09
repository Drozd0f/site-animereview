from django.contrib import admin

from .models import *

# Register your models here.


admin.site.register(Universe)
admin.site.register(User)


class PostsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Posts, PostsAdmin)
admin.site.register(Genre, GenreAdmin)
