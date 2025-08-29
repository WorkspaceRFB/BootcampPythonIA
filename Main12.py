import funcoes
print(funcoes.maiorIdade(19))

tarefas = []

addTarefas = input('Deseja adicionar uma tarefa? S/N: ')

while addTarefas == 'S':
    tarefas.append(input('Qual a tarefa? '))
    addTarefas = input('Deseja adicionar uma tarefa? S/N: ')

x = 1
for tarefa in tarefas:
    print(f'Tarefa', x, '-', tarefa)
    x = x+1
