from django.contrib import admin
from products.models import ProductCategory, Products

admin.site.register(ProductCategory)


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity')
    search_fields = ('name',)
    fields = ('name', 'image', 'description', ('price', 'quantity', 'category'))
    readonly_fields = ('quantity',)
    ordering = ('-price',)
