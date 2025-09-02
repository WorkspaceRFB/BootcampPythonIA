import pooCasa16

casa1 = pooCasa16.Casa('Preta', 2, 3)
casa2 = pooCasa16.Casa('Verde', 3, 4)

print(casa1.mostrarCor(),',',
      casa1.mostrarQuartos(), 'e',
      casa1.mostrarBanheiros())
print(casa1.construirQuarto())
print(casa1.pintarCasa('Azul'))

print(casa2.mostrarCor(),',',
      casa2.mostrarQuartos(), 'e',
      casa2.mostrarBanheiros())
print(casa2.construirQuarto())
