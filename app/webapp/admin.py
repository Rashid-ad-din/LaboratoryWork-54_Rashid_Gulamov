from django.contrib import admin
from webapp.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'created_at', 'changed_at')
    list_filter = ('category', 'created_at', 'changed_at')
    search_fields = 'category'
    fields = ('category', 'created_at', 'changed_at')
    readonly_fields = ('id', 'created_at', 'changed_at')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'created_at', 'changed_at')
    list_filter = ('title', 'price', 'category')
    search_fields = ('title', 'category')
    fields = ('title', 'category', 'description', 'created_at', 'changed_at')
    readonly_fields = ('id', 'created_at', 'changed_at')

