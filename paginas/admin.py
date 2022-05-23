from django.contrib import admin

# Register your models here.

from .models import Cidade, Funcionario

admin.site.register(Cidade)
admin.site.register(Funcionario)
