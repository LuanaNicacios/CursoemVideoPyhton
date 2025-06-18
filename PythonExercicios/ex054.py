from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(1, 8):
    nascimento = int(input('Em que ano a {} pessoa nasceu? '.format(pessoa)))
    idade = atual - nascimento
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E tivemos {} menores de idade'.format(totmenor))