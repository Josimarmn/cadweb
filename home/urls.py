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
    path('produto', views.produto, name='produto'),
    path('form_produto', views.form_produto, name='form_produto'),
    path('editar_produto/<int:id>/',views.editar_produto, name='editar_produto'),
    path('remover_produto/<int:id>/',views.remover_produto, name='remover_produto'),
    path('detalhes_produto/<int:id>/',views.detalhes_produto, name='detalhes_produto'),
    path('ajustar_estoque/<int:id>/',views.ajustar_estoque, name='ajustar_estoque'),
    path('teste1/', views.teste1, name='teste1'),
    path('teste2/', views.teste2, name='teste2'),
    path('buscar_dados/<str:app_modelo>/', views.buscar_dados, name="buscar_dados"),
    path('teste3/', views.teste3, name='teste3'),
    path('pedido', views.pedido, name='pedido'),
    path('novo_pedido/<int:id>', views.novo_pedido, name="novo_pedido"),
    path('detalhes_pedido/<int:id>/',views.detalhes_pedido, name='detalhes_pedido'),
    path('remover_item_pedido/<int:id>/', views.remover_item_pedido, name='remover_item_pedido'),
    path('editar_item_pedido/<int:id>/', views.editar_item_pedido, name='editar_item_pedido'),
    path('remover_pedido/<int:id>/',views.remover_pedido, name='remover_pedido'),
    path('form_pagamento/<int:id>/',views.form_pagamento, name='form_pagamento'),

]
