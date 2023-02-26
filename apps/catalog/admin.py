from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_img', 'name', 'created']

    def get_img(self, obj):
        return mark_safe(f'<img src="{obj.poster.url}" width=150 height=150>')


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['product']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category']


@admin.register(Review)
class Review(admin.ModelAdmin):
    list_display = ['user']


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['material']


@admin.register(Brand)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['brand']


