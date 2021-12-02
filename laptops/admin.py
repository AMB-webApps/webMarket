from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'brand',
        'name',
        'display',
        'cpu',
        'memory',
        'ssd_hdd',
        'graphic_card',
        'uses',
        'model',
        'price',
        'image',
    )
    list_display_links = ('id', 'name')
    search_fields = ('brand', 'name', 'uses')
