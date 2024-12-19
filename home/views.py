from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
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
            categoria = form.save() # salva a instancia do modelo no banco de dados
            messages.success(request, 'Operação realizada com sucesso!')
            return redirect('categoria') # redireciona para a listagem
    else:# método é get, novo registro
        form = CategoriaForm() # formulário vazio
    contexto = {
        'form':form,
    }
    return render(request, 'categoria/formulario.html', contexto)


def editar_categoria(request, id):
    try:
        categoria = Categoria.objects.get(pk=id)
    except Categoria.DoesNotExist:
        # Caso o registro não seja encontrado, exibe a mensagem de erro
        messages.error(request, 'Registro não encontrado')
        return redirect('categoria')  # Redireciona para a listagem


    if request.method == 'POST':
        # combina os dados do formulário submetido com a instância do objeto existente, permitindo editar seus valores.
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            categoria = form.save() # save retorna o objeto salvo
            messages.success(request, 'Operação realizada com Sucesso')
            return redirect('categoria')
    else:
        form = CategoriaForm(instance=categoria)
        
    return render(request, 'categoria/formulario.html', {'form': form,})


from django.contrib import messages
from django.shortcuts import redirect
from .models import Categoria

def remover_categoria(request, id):
    try:
        # Tenta obter a categoria com o id fornecido
        categoria = Categoria.objects.get(pk=id)
        categoria.delete()  # Exclui a categoria encontrada
        messages.success(request, 'Operação realizada com sucesso')  # Exibe mensagem de sucesso
    except Categoria.DoesNotExist:
        # Caso o registro não seja encontrado, exibe a mensagem de erro
        messages.error(request, 'Registro não encontrado')
    
    return redirect('categoria')  # Redireciona para a listagem de categorias
           

def detalhes_categoria(request, id):
    categoria = Categoria.objects.get(pk=id)  
    return render(request, 'categoria/detalhes.html', {'categoria':categoria})

def clean_nome(self):
    nome = self.cleaned_data.get('nome')
    if len(nome) < 3:
        raise forms.ValidationError("O nome deve ter pelo menos 3 caracteres.")
    return nome  
    
def clean_ordem(self):
    ordem = self.cleaned_data.get('ordem')
    if ordem <= 0:
        raise forms.ValidationError("O campo ordem deve ser maior que zero.")
    return ordem


