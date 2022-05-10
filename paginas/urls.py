from django.urls import path
from .views import CidadeCreate, PessoaCreate
from .views import CidadeUpdate, PessoaUpdate

urlpatterns = [
    path('cadastrar/cidade/', CidadeCreate.as_view(), name='cadastrar-cidade'),
    path('cadastrar/pessoa/', PessoaCreate.as_view(), name='cadastrar-pessoa'),

    path('editar/pessoa/<int:pk>/', PessoaUpdate.as_view(), name='editar-pessoa'),
    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name='editar-cidade'),

]
