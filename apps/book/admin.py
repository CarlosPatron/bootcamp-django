import imp
from django.contrib import admin
from apps.book.models import Category, Book

# Register your models here.
admin.site.register(Category)
admin.site.register(Book)