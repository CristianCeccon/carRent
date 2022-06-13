from dataclasses import fields
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from braces.views import GroupRequiredMixin

from .models import Cidade, Funcionario, Usuario

# Create your views here.


class CidadeCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')


class FuncionarioCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Funcionario
    group_required = u"Administrador"
    fields = ['nome_completo', 'email','nascimento' ]
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-funcionario')
    #login_url = reverse_lazy('login')


class CidadeUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')


class FuncionarioUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Funcionario
    fields = ['nome_completo', 'email', 'nascimento', 'contato']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-funcionario')


class Index(GroupRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = "paginas/index.html"


class Perfil(GroupRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = "paginas/perfil.html"


class FuncionarioDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Funcionario
    group_required = u"Administrador"
    template_name = 'paginas/form-delete.html'
    sucess_url = reverse_lazy('listar-funcionario')


class CidadeDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Cidade
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('index')


class FuncionarioList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Funcionario
    template_name = 'paginas/listas/pessoas.html'


class UsuarioCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Usuario
    group_required = u"Usuario"
    template_name = 'static/users-profile.html'
