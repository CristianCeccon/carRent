from django.contrib import admin

# Register your models here.

from .models import Cidade, Pessoa

admin.site.register(Cidade)
admin.site.register(Pessoa)
