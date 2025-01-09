from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('categoria', views.categoria, name="categoria"),
    path('form_categoria', views.form_categoria, name="form_categoria"),
    path('editar_categoria/<int:id>/',views.editar_categoria, name='editar_categoria'),
    path('detalhes_categoria/<int:id>/',views.detalhes_categoria, name='detalhes_categoria'),
    path('remover_categoria/<int:id>/',views.remover_categoria, name='remover_categoria'),
    path('cliente', views.cliente, name="cliente"),
    path('form_cliente', views.form_cliente, name="form_cliente"),
    path('editar_cliente/<int:id>/',views.editar_cliente, name='editar_cliente'),
    path('remover_cliente/<int:id>/',views.remover_cliente, name='remover_cliente'),
    path('produto/', views.produto, name='produto'),
    path('form_produto/', views.form_produto, name='form_produto'),
    path('editar_produto/<int:id>/',views.editar_produto, name='editar_produto'),
    path('remover_produto/<int:id>/',views.remover_produto, name='remover_produto'),
]
