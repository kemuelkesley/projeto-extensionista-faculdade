from django.contrib import admin
from . models import Operacional, Tecnico, Condominio ,Categoria, Sobre


class OperacionalAdmin(admin.ModelAdmin):
    list_display = ('title', 'activate', 'created_at')   
    list_filter = ('title', 'activate', 'created_at')
    date_hierarchy = 'created_at'
    ordering = ('title', 'created_at')   
    readonly_fields = ('created_at',)



class TecnicoAdmin(admin.ModelAdmin):
    list_display = ('title',  'description',) 
    ordering = ('title',)
   


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'activate')   
    list_filter = ('title', 'activate', 'created_at')
    date_hierarchy = 'created_at'
    ordering = ('title', 'created_at')   
    readonly_fields = ('created_at',)



class CondominoAdmin(admin.ModelAdmin):
    list_display = ('condominium_number', 'condominium_name', 'title', 'created_at', 'activate',)



class SobreAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    ordering = ('description', 'created_at')   
    readonly_fields = ('created_at',)


admin.site.register(Operacional, OperacionalAdmin)
admin.site.register(Tecnico, TecnicoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Condominio, CondominoAdmin)
admin.site.register(Sobre, SobreAdmin)

