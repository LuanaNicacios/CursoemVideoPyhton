from datetime import date
nascimento = int(input('Digite o ano de nascimento: ' ))
atual = date.today().year
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Atleta classificação: MIRIM')
elif idade <= 14:
    print('Atleta classificação: INFANTIL')
elif idade <= 19:
    print('Atleta classificação: JUNIOR')
elif idade <= 25:
    print('Atleta classificação: SÊNIOR')
else:
    print('Atleta classificação: MASTER')
