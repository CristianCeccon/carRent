from dataclasses import fields
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .models import Cidade, Funcionario

# Create your views here.


class CidadeCreate(CreateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')


class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome_completo', 'email','nascimento' ]
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-funcionario')


class CidadeUpdate(UpdateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')


class FuncionarioUpdate(UpdateView):
    model = Funcionario
    fields = ['nome_completo', 'email', 'nascimento', 'contato']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-funcionario')


class Index(TemplateView):
    template_name = "carRent/static/index.html"


class FuncionarioDelete(DeleteView):
    model = Funcionario
    template_name = 'paginas/form-delete.html'
    sucess_url = reverse_lazy('listar-funcionario')


class CidadeDelete(DeleteView):
    model = Cidade
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('index')


class FuncionarioList(ListView):
    model = Funcionario
    template_name = 'paginas/listas/pessoas.html'