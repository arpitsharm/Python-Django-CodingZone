from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(ContactUs)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'phone_num']

admin.site.register(Apps)