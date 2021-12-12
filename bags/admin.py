from django.contrib import admin
from .models import Bags


class BagsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'image',
        'color',
        'material',
        'price',
    )


admin.site.register(Bags, BagsAdmin)
