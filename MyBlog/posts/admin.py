from django.contrib import admin
from django.contrib.admin import register

from .models import Post #class ismini yazmayı unutma
# Register your models here.
admin.site.register(Post)
