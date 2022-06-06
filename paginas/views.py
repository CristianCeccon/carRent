from dataclasses import fields
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Cidade, Funcionario, Usuario

# Create your views here.


class CidadeCreate(LoginRequiredMixin, CreateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')


class FuncionarioCreate(LoginRequiredMixin, CreateView):
    model = Funcionario
    fields = ['nome_completo', 'email','nascimento' ]
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-funcionario')
    #login_url = reverse_lazy('login')


class CidadeUpdate(LoginRequiredMixin, UpdateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')


class FuncionarioUpdate(LoginRequiredMixin, UpdateView):
    model = Funcionario
    fields = ['nome_completo', 'email', 'nascimento', 'contato']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-funcionario')


class Index(LoginRequiredMixin, TemplateView):
    template_name = "paginas/index.html"


class Perfil(LoginRequiredMixin, TemplateView):
    template_name = "paginas/perfil.html"


class FuncionarioDelete(LoginRequiredMixin, DeleteView):
    model = Funcionario
    template_name = 'paginas/form-delete.html'
    sucess_url = reverse_lazy('listar-funcionario')


class CidadeDelete(LoginRequiredMixin, DeleteView):
    model = Cidade
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('index')


class FuncionarioList(LoginRequiredMixin, ListView):
    model = Funcionario
    template_name = 'paginas/listas/pessoas.html'


class UsuarioCreate(LoginRequiredMixin, CreateView):
    model = Usuario
    template_name = 'static/users-profile.html'
