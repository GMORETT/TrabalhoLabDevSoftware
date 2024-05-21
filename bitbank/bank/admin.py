from django.contrib import admin
from .models import Conta

class ContaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'saldo_real', 'saldo_bitcoin', 'saldo_ethereum')


admin.site.register(Conta, ContaAdmin)