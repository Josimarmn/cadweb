from django.shortcuts import render, redirect
from .models import *
from .forms import *

from .models import Categoria

def index(request):
    return render(request,'index.html')

def categoria(request):
    contexto = {
        'lista': Categoria.objects.all().order_by('id'),
    }
    return render(request, 'categoria/lista.html',contexto)

def form_categoria(request):
    if request.method == 'POST':
       form = CategoriaForm(request.POST) # instancia o modelo com os dados do form
       if form.is_valid():# faz a validação do formulário
            form.save() # salva a instancia do modelo no banco de dados
            return redirect('categoria') # redireciona para a listagem
    else:# método é get, novo registro
        form = CategoriaForm() # formulário vazio
    contexto = {
        'form':form,
    }
    return render(request, 'categoria/formulario.html', contexto)

def detalhes_produto(request, id):
    form = CategoriaForm()
    contexto = {
        'form':form,
    }
    return render(request, 'categoria/formulario.html', contexto)

def editar_produto(request, id):
    form = CategoriaForm()
    contexto = {
        'form':form,
    }
    return render(request, 'categoria/formulario.html', contexto)

def excluir_produto(request, id):
    form = CategoriaForm()
    contexto = {
        'form':form,
    }
    return render(request, 'categoria/formulario.html', contexto)

def editar_categoria(request, id):
    categoria = Categoria.objects.get(pk=id)
    if request.method == 'POST':
        # combina os dados do formulário submetido com a instância do objeto existente, permitindo editar seus valores.
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            categoria = form.save() # save retorna o objeto salvo
            return redirect('categoria') # redireciona para a listagem
    else:
         form = CategoriaForm(instance=categoria)
    return render(request, 'categoria/formulario.html', {'form': form,})

def remover_categoria(request, id):
    form = CategoriaForm()
    contexto = {
        'form':form,
    }
    return render(request, 'categoria/formulario.html', contexto)

def detalhes_categoria(request, id):
    form = CategoriaForm()
    contexto = {
        'form':form,
    }
    return render(request, 'categoria/formulario.html', contexto)

