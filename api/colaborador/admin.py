from django.contrib import admin

from colaborador.models import Cargo, Colaborador, Genero


@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ativo', 'cpf', 'data_nascimento',
                    'telefone', 'Cargo', 'Genero']
    search_fields = ['nome', 'cpf']


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'salario']
    search_fields = ['nome']


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']
