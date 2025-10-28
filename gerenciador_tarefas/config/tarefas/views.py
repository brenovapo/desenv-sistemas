from django.shortcuts import get_object_or_404, redirect, render
from .models import Tarefas
from django.http import HttpResponse

def listar_tarefas(request):
    tarefas_salvas = Tarefas.objects.all()
    contexto = {
      "minhas_tarefas": tarefas_salvas
    }
    return render(request, 'tarefas/lista.html', contexto)

def detalhe_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefas, pk=tarefa_id)

    return render(request, 'tarefas/detalhe.html', {'tarefa': tarefa})


def adicionar_tarefa (request):
  if request.method == 'POST':
    titulo = request.POST.get('titulo')
    descricao = request.POST.get('descricao')
    Tarefas.objects.create(titulo=titulo,descricao=descricao)
    return redirect('listar_tarefas')

  return render (request,'tarefas/form_tarefa.html')


def alterar_tarefa(request, tarefa_id):
  tarefa= get_object_or_404(Tarefas, pk= tarefa_id)
  if request.method == 'POST':
    tarefa.titulo = request.POST.get('titulo')
    tarefa.descricao = request.POST.get('descricao')
    tarefa.concluida = request.POST.get('concluida') == 'on'
    tarefa.save() #salva as alterações no objeto existente 
    return redirect ('listar_tarefas')
  return render(request,'tarefas/form_tarefa.html', {'tarefa':tarefa})



    