from django.contrib import admin
from blog.models import *

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tiny.js',)
    list_display = ['title', 'author', 'slug', 'views']

admin.site.register(BlogComment)