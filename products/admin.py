from django.contrib import admin

from products.models import CategoryModel, BrandModel, ProductTagModel, ProductModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(BrandModel)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(ProductTagModel)
class ProductTagModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'brand', 'price', 'discount', 'short_description', 'created_at']
    search_fields = ['title', 'category__title', 'short_description']
    list_filter = ['category', 'brand', 'tags', 'created_at']
    autocomplete_fields = ['category', 'brand', 'tags']
