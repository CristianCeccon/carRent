from dataclasses import fields
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from .models import Cidade, Pessoa

# Create your views here.


class CidadeCreate(CreateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')


class PessoaCreate(CreateView):
    model = Pessoa
    fields = ['nome_completo', 'email','nascimento' ]
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')


class CidadeUpdate(UpdateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')


class PessoaUpdate(UpdateView):
    model = Pessoa
    fields = ['nome_completo', 'email', 'nascimento']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')


class Index(TemplateView):
    template_name = "paginas/modelo.html"