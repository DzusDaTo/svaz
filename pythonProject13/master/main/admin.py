from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


class SvazAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email', 'data_roj', 'foto', 'otvet')
    list_display_links = ('last_name', 'first_name')
    search_fields = ('last_name', 'first_name', 'data_roj')
    list_filter = ('last_name', 'first_name', 'data_roj')
    list_editable = ('otvet',)
    fields = ('last_name', 'first_name', 'biografy', 'data_roj', 'email', 'image', 'foto', 'otvet')
    readonly_fields = ('foto',)

    def foto(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=100")

    foto.short_description = 'Миниатюра'


admin.site.register(Svaz, SvazAdmin)
