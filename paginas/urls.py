from django.urls import path
from .views import CidadeCreate, FuncionarioCreate, Perfil
from .views import CidadeUpdate, FuncionarioUpdate
from .views import CidadeDelete, FuncionarioDelete
from .views import Index
from .views import FuncionarioList
from .views import UsuarioCreate

urlpatterns = [
    path('cadastrar/cidade/', CidadeCreate.as_view(), name='cadastrar-cidade'),
    path('cadastrar/funcionario/', FuncionarioCreate.as_view(), name='cadastrar-funcionario'),
    path('cadastrar/usuario/', UsuarioCreate.as_view(), name='cadastrar-usuario'),


    path('editar/funcionario/<int:pk>/', FuncionarioUpdate.as_view(), name='editar-funcionario'),
    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name='editar-cidade'),

    path('excluir/funcionario/<int:pk>/', FuncionarioDelete.as_view(), name='excluir-funcionario'),
    path('excluir/cidade/<int:pk>/', CidadeDelete.as_view(), name='excluir-cidade'),

    path('listar/funcionario/', FuncionarioList.as_view(), name='listar-funcionario'),

    path('menu/', Index.as_view(), name='menu'),

    path('perfil/', Perfil.as_view(), name='perfil'),

]
