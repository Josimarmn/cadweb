from django.shortcuts import render
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
    form = CategoriaForm()
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
