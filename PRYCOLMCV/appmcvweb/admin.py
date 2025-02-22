from django.contrib import admin
from .models import grupo
from .models import inicio

admin.site.site_header = "COLEGIO MANUEL CEPEDA VARGAS"
admin.site.index_title = "ACTUALIZACION DE LA PAGINA WEB"
admin.site.site_title = "COL MCV IED"

# Register your models here.

@admin.register(grupo)
class grupoadmin(admin.ModelAdmin):
    list_display = ('nombre', 'updated' )

@admin.register(inicio)
class inicioadmin(admin.ModelAdmin):
    list_display = ('titulo', 'grupo', 'enlace', 'updated')
    ordering = ['updated']
    search_fields = ['titulo']
    list_editable = ['grupo']
    list_filter =  ['grupo']
    list_per_page = 5



