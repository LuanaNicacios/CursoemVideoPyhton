"""Utilizando condições simples"""

nome = str(input('Qual é o seu nome? ')).upper()
if nome == 'AGNA':
    print('Que nome lindo você tem')
else:
    print('Seu nome é tão normal')
print('Bom dia, {}'.format(nome))