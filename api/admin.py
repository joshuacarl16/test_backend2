from django.contrib import admin
from .models import Category, Topic, Comment

admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(Comment)