from random import choice
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo Aluno: '))
a3 = str(input('Terceiro Aluno: '))
a4 = str(input('Quarto Aluno: '))

lista = [a1, a2, a3, a4]
esc = choice(lista)

print('O aluno escolhido foi: {}'.format(esc))
