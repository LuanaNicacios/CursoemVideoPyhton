from datetime import date
anonasc = int(input('Digite o ano do seu nascimento: '))
idade = date.today().year - anonasc
print('Você tem: \033[1;32m{} anos!\033[m'.format(idade))
if idade == 18:
    print('\033[1;33mEstá na hora de se alistar!\033[m')
elif idade > 18:
    print('E já passou, \033[1;31m{} anos\033[m do prazo de seu alistameto!'.format(idade - 18))
else:
    print('Você ainda não completou \033[1;32m 18 anos\033[m, ainda faltam \033[1;33m{}\033[m anos para seu alistamento.'.format(18 - idade))

#CÓDIGO DO GUANABARA#
'''
from datetime import date
atual = date.today().year
nasc = int(input('Ano de seu nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print ('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))
'''