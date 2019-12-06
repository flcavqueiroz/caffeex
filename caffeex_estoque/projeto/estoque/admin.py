from django.contrib import admin
from .models import EstoqueEntrada, EstoqueSaida, EstoqueItens


class EstoqueItensInline(admin.TabularInline):
    model = EstoqueItens
    extra = 0


@admin.register(EstoqueEntrada)
class EstoqueEntradaAdmin(admin.ModelAdmin):
    inlines = (EstoqueItensInline,)
    list_display = ('__str__', 'safra', 'funcionario',)
    search_fields = ('safra',)
    list_filter = ('funcionario',)
    date_hierarchy = 'created'


@admin.register(EstoqueSaida)
class EstoqueSaidaAdmin(admin.ModelAdmin):
    inlines = (EstoqueItensInline,)
    list_display = ('__str__', 'safra', 'funcionario',)
    search_fields = ('safra',)
    list_filter = ('funcionario',)
    date_hierarchy = 'created'
