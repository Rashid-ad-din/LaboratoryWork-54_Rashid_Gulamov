from django.contrib import admin
from webapp.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'created_at', 'changed_at')
    list_filter = ('category',)
    search_fields = ('category',)
    fields = ('category', 'description')
    readonly_fields = ('id', 'created_at', 'changed_at')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'image', 'category', 'created_at', 'changed_at')
    list_filter = ('title', 'price', 'category')
    search_fields = ('title', 'category')
    fields = ('title', 'price', 'image', 'category', 'description')
    readonly_fields = ('id', 'created_at', 'changed_at')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
