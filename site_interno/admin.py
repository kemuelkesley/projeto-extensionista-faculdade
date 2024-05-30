from django.contrib import admin
from . models import Operacional, Sobre


class OperacionalAdmin(admin.ModelAdmin):
    list_display = ('title', 'activate', 'created_at')   
    list_filter = ('title', 'activate', 'created_at')
    date_hierarchy = 'created_at'
    ordering = ('title', 'created_at')   
    readonly_fields = ('created_at',)



class SobreAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    ordering = ('description', 'created_at')   
    readonly_fields = ('created_at',)


admin.site.register(Operacional, OperacionalAdmin)
admin.site.register(Sobre, SobreAdmin)


