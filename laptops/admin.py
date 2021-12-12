# Username: adminnn
# Password: admin1212

from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'brand',
        'name',
        'uses',
        'price',
        'image',
    )
    include = ('display',
               'cpu',
               'memory',
               'ssd_hdd',
               'graphic_card',
               'uses',
               'model'
               )

    list_display_links = ('id', 'name')
    search_fields = ('brand', 'name', 'uses')
