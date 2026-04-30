from django.urls import path
from . import views

urlpatterns = [
    path('', views.calcular_imc, name='calculadora_imc'),
    path('pagina2/', views.pagina2, name='pagina2'),
    path('pagina3/', views.pagina3, name='pagina3'),
    path('pagina4/', views.pagina4, name='pagina4'),
    path('pagina5/', views.pagina5, name='pagina5'),
    path('pagina6/', views.pagina6, name='pagina6'),
    path('hamburguer/', views.pagina7, name='hamburguer'),  
]