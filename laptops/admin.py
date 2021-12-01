from django.contrib import admin


class ProductAdmin(admin.ModelAdmin):
    list_display = [
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
    ]