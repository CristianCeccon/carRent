from django.urls import path
from .views import Index

urlpatterns = [
    path(
        '',          # vai no navegador
        Index.as_view(),    
        name='index',       # apenas o nome dela
    ),
]
