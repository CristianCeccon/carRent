from os import path
from .views import CidadeCreate, PessoaCreate
from .views import CidadeUpdate, PessoaUpdate

urlpatterns = [
    path('paginas/cidade/', CidadeCreate.as_view(), name='cadastrar-cidade'),
    path('paginas/pessoa/', PessoaCreate.as_view(), name='cadastrar-pessoa'),

    path('editar/estado/<int:pk>/', PessoaUpdate.as_view(), name='editar-pessoa'),
    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name='editar-cidade'),

]
