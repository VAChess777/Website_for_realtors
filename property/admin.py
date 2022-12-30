from django.contrib import admin

from .models import Flat


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ('created_at', )
    list_display = (
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
        'created_at'
    )
    list_editable = ('new_building',)


# admin.site.register(Flat, FlatAdmin)



















